#!/usr/bin/env python3

import sys
import win32com.client
import os

EXCEL_FILE_PATH = sys.argv[1]
PDF_FILE_PATH = sys.argv[2]

EXCEL_FILE_ABSOLUTE_PATH = os.path.abspath(EXCEL_FILE_PATH)
PDF_FILE_ABSOLUTE_PATH = os.path.abspath(PDF_FILE_PATH)

print(f"Excel File Path: {EXCEL_FILE_PATH}")
print(f"PDF File Path: {PDF_FILE_PATH}")

print(f"Absolute Excel File Path: {EXCEL_FILE_ABSOLUTE_PATH}")
print(f"Absolute PDF File Path: {PDF_FILE_ABSOLUTE_PATH}")

try:
    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = False

    wb = o.Workbooks.Open(EXCEL_FILE_ABSOLUTE_PATH)
    wb.ExportAsFixedFormat(0, PDF_FILE_ABSOLUTE_PATH)

    wb.Close(True)
except Exception as e:
    print('PDF Export Failed!')
    raise e
else:
    print('PDF Export Succeeded!')