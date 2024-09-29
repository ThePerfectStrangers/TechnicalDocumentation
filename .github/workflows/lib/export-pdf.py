#!/usr/bin/env python3

import sys
import win32com.client

EXCEL_FILE_PATH = sys.argv[1]
PDF_FILE_PATH = sys.argv[2]

print(f"Excel File Path: {EXCEL_FILE_PATH}")
print(f"PDF File Path: {PDF_FILE_PATH}")

try:
    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = False

    wb = o.Workbooks.Open(EXCEL_FILE_PATH)
    wb.ExportAsFixedFormat(0, PDF_FILE_PATH)

    wb.Close(True)
except Exception as e:
    print('PDF Export Failed!')
    raise e
else:
    print('PDF Export Succeeded!')