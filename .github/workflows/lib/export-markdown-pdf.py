#!/usr/bin/env python3
"""
Converts a Markdown file to PDF using md2pdf (Chromium-based rendering).

This handles embedded HTML (tables, images, etc.) that commonly appears
in Markdown files, producing a faithful PDF representation.

Usage:
    python export-markdown-pdf.py <input.md> <output.pdf>

Arguments:
    input   - Absolute path to the Markdown file
    output  - Absolute path to the output PDF file
"""

import sys
import os
from md2pdf.core import md2pdf


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.md> <output.pdf>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    print(f"Converting: {input_path}")
    print(f"Output: {output_path}")

    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    # Read the markdown content
    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Use the input file's directory as the base path for resolving relative
    # image references (e.g. ../Assets/Logo/Logo.png)
    base_dir = os.path.dirname(input_path)

    md2pdf(
        output_path,
        md_content=md_content,
        md_file_path=input_path,
        base_url=base_dir,
    )

    if os.path.exists(output_path):
        print(f"Successfully generated: {output_path}")
    else:
        print("Failed to generate PDF")
        sys.exit(1)


if __name__ == '__main__':
    main()
