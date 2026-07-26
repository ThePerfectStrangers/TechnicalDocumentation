#!/usr/bin/env python3
"""
Exports a Draw.io diagram to PNG or PDF, optionally restricting the export to
a subset of layers.

Layer visibility is controlled by modifying the XML directly (setting
visible="0"/"1" on layer cells) rather than relying on drawio's --layers CLI
flag, mirroring the (more reliable) approach used by
export-drawio-layered-gif.py.

Usage:
    python export-drawio.py <drawio_path> <output_path> <format> [layers]

Arguments:
    drawio_path  - Absolute path to the .drawio file
    output_path  - Absolute path for the exported file
    format       - Export format (png or pdf)
    layers       - Optional comma-separated list of 0-based layer indices to
                   export (e.g. "0,1,3"). If omitted or empty, all layers are
                   exported.
"""

import os
import subprocess
import sys
import xml.etree.ElementTree as ET


def restrict_layers(drawio_path, layer_indices):
    """Write a temp copy of the diagram with only the given layers visible.

    Returns the path to use as export input. If layer_indices is None, the
    original path is returned unchanged since no filtering is needed.
    """
    if layer_indices is None:
        return drawio_path

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

    output_dir = os.path.dirname(os.path.abspath(drawio_path))
    tmp_path = os.path.join(output_dir, f'_tmp_{os.getpid()}.drawio')
    tree.write(tmp_path, encoding='unicode')
    return tmp_path


def export(drawio_path, output_path, export_format, layer_indices):
    export_input = restrict_layers(drawio_path, layer_indices)
    try:
        env = os.environ.copy()
        env['ELECTRON_EXTRA_LAUNCH_ARGS'] = '--no-sandbox --disable-gpu'

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        result = subprocess.run(
            [
                'drawio', '--export',
                '--format', export_format,
                '--output', output_path,
                export_input,
            ],
            capture_output=True,
            text=True,
            env=env,
        )

        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr)
            result.check_returncode()

        # draw.io sometimes appends a -0 page-index suffix (e.g. Diagram-0.png)
        if not os.path.exists(output_path):
            base, ext = os.path.splitext(output_path)
            page_indexed = f"{base}-0{ext}"
            if os.path.exists(page_indexed):
                os.rename(page_indexed, output_path)
            else:
                dir_contents = os.listdir(os.path.dirname(output_path))
                raise FileNotFoundError(
                    f"draw.io exited 0 but output file was not created.\n"
                    f"  Expected: {output_path}\n"
                    f"  Directory contents: {dir_contents}\n"
                    f"  STDOUT: {result.stdout}\n"
                    f"  STDERR: {result.stderr}"
                )
    finally:
        if export_input != drawio_path and os.path.exists(export_input):
            os.remove(export_input)


def main():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <drawio_path> <output_path> <format> [layers]")
        sys.exit(1)

    drawio_path = sys.argv[1]
    output_path = sys.argv[2]
    export_format = sys.argv[3]
    layers_arg = sys.argv[4] if len(sys.argv) > 4 else ''

    layer_indices = None
    if layers_arg.strip():
        layer_indices = {int(x.strip()) for x in layers_arg.split(',') if x.strip() != ''}

    print(f"Draw.io file: {drawio_path}")
    print(f"Output path: {output_path}")
    print(f"Format: {export_format}")
    print(f"Layers: {sorted(layer_indices) if layer_indices is not None else 'all'}")

    try:
        export(drawio_path, output_path, export_format, layer_indices)
    except Exception as e:
        print('Export Failed!')
        raise e
    else:
        print('Export Succeeded!')


if __name__ == '__main__':
    main()
