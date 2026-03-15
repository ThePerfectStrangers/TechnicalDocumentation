#!/usr/bin/env python3
"""
Exports a Draw.io diagram as an animated GIF showing cumulative layer assembly,
along with individual step PNGs that build upon each other.

Layers are discovered from the XML and sorted naturally by name.
Each step shows all layers up to and including the current one.

Usage:
    python export-drawio-layered-gif.py <drawio_path> <output_dir> [frame_duration_ms]

Arguments:
    drawio_path       - Absolute path to the .drawio file
    output_dir        - Absolute path to the output directory
    frame_duration_ms - Milliseconds per frame in the GIF (default: 1000)
"""

import sys
import os
import re
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image


def natural_sort_key(text):
    """Sort key that handles embedded numbers naturally (e.g. '2. Foo' before '10. Bar')."""
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r'(\d+)', text)]


def parse_layers(drawio_path):
    """
    Discover layers in a drawio file.

    Layers are mxCell elements with parent="0" (excluding the root cell id="0").
    Returns a list of (xml_index, layer_name) tuples sorted naturally by name.
    The xml_index is the 0-based position among layer cells in the XML,
    which corresponds to drawio's --layers CLI index.
    """
    tree = ET.parse(drawio_path)
    root = tree.getroot()
    layers = []
    xml_index = 0

    for diagram in root.findall('diagram'):
        model = diagram.find('mxGraphModel')
        if model is None:
            continue
        root_elem = model.find('root')
        if root_elem is None:
            continue
        for cell in root_elem.findall('mxCell'):
            if cell.get('parent') == '0' and cell.get('id') != '0':
                layers.append((xml_index, cell.get('value', '')))
                xml_index += 1

    layers.sort(key=lambda x: natural_sort_key(x[1]))
    return layers


def export_to_png(drawio_path, png_path, layer_indices):
    """Export the drawio file to PNG with only the specified layers visible.

    Layer visibility is controlled by modifying the XML directly rather than
    using the --layers CLI flag.

    Chromium flags (--no-sandbox, --disable-gpu) are passed via the
    ELECTRON_EXTRA_LAUNCH_ARGS env-var because draw.io 26.x's own arg parser
    treats unrecognised CLI flags as the input-file positional argument.
    """
    # Build a modified copy of the diagram with only the target layers visible.
    tree = ET.parse(drawio_path)
    xml_root = tree.getroot()
    xml_index = 0
    for diagram in xml_root.findall('diagram'):
        model = diagram.find('mxGraphModel')
        if model is None:
            continue
        root_elem = model.find('root')
        if root_elem is None:
            continue
        for cell in root_elem.findall('mxCell'):
            if cell.get('parent') == '0' and cell.get('id') != '0':
                cell.set('visible', '1' if xml_index in layer_indices else '0')
                xml_index += 1

    # Write the modified diagram next to the output (same filesystem the
    # runner can always reach) and clean up afterwards.
    output_dir = os.path.dirname(png_path)
    os.makedirs(output_dir, exist_ok=True)
    tmp_input = os.path.join(output_dir, f'_tmp_{os.getpid()}.drawio')
    tree.write(tmp_input, encoding='unicode')

    try:
        env = os.environ.copy()
        env['ELECTRON_EXTRA_LAUNCH_ARGS'] = '--no-sandbox --disable-gpu'

        result = subprocess.run(
            [
                'drawio', '--export',
                '--no-sandbox',
                '--disable-gpu',
                '--format', 'png',
                '--output', png_path,
                tmp_input,
            ],
            capture_output=True,
            text=True,
            env=env,
        )

        if result.returncode != 0:
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            result.check_returncode()

        # draw.io sometimes appends a -0 page-index suffix (e.g. Step_01-0.png)
        if not os.path.exists(png_path):
            base, ext = os.path.splitext(png_path)
            page_indexed = f"{base}-0{ext}"
            if os.path.exists(page_indexed):
                os.rename(page_indexed, png_path)
            else:
                dir_contents = os.listdir(output_dir)
                raise FileNotFoundError(
                    f"draw.io exited 0 but output file was not created.\n"
                    f"  Expected: {png_path}\n"
                    f"  Directory contents: {dir_contents}\n"
                    f"  STDOUT: {result.stdout}\n"
                    f"  STDERR: {result.stderr}"
                )
    finally:
        if os.path.exists(tmp_input):
            os.remove(tmp_input)


def create_gif(png_paths, gif_path, frame_duration):
    """Combine a sequence of PNGs into an animated GIF."""
    frames = []
    for path in png_paths:
        img = Image.open(path)
        if img.mode == 'RGBA':
            bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg.convert('RGB')
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        frames.append(img)

    if not frames:
        return

    # Hold the last frame 3x longer so the completed diagram is visible
    durations = [frame_duration] * len(frames)
    durations[-1] = frame_duration * 3

    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
    )


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <drawio_path> <output_dir> [frame_duration_ms]")
        sys.exit(1)

    drawio_path = sys.argv[1]
    output_dir = sys.argv[2]
    frame_duration = int(sys.argv[3]) if len(sys.argv) > 3 else 1000

    print(f"Draw.io file: {drawio_path}")
    print(f"Output directory: {output_dir}")
    print(f"Frame duration: {frame_duration}ms")

    # Discover and sort layers
    layers = parse_layers(drawio_path)
    print(f"\nFound {len(layers)} layers (sorted):")
    for xml_idx, name in layers:
        print(f"  [{xml_idx}] {name}")

    if not layers:
        print("No layers found. Exiting.")
        sys.exit(0)

    # Prepare output directory
    os.makedirs(output_dir, exist_ok=True)

    # Clean previous generated files
    for f in os.listdir(output_dir):
        full_path = os.path.join(output_dir, f)
        if os.path.isfile(full_path) and (f.endswith('.png') or f.endswith('.gif')):
            os.remove(full_path)

    # Export cumulative layer PNGs
    pad = len(str(len(layers)))
    png_paths = []

    for step in range(1, len(layers) + 1):
        visible_indices = [layers[j][0] for j in range(step)]
        step_label = f"Step_{str(step).zfill(pad)}"
        png_path = os.path.join(output_dir, f"{step_label}.png")

        print(f"\nExporting {step_label} (layers: {visible_indices})...")
        export_to_png(drawio_path, png_path, visible_indices)
        png_paths.append(png_path)
        print(f"  Saved: {png_path}")

    # Create animated GIF
    gif_name = os.path.splitext(os.path.basename(drawio_path))[0] + ".gif"
    gif_path = os.path.join(output_dir, gif_name)
    print(f"\nCreating animated GIF: {gif_path}")
    create_gif(png_paths, gif_path, frame_duration)

    print("\nDone!")


if __name__ == '__main__':
    main()
