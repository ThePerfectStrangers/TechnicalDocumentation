#!/usr/bin/env python3

import sys
import win32com.client
from PIL import ImageGrab

EXCEL_FILE_PATH = sys.argv[1]
OUTPUT_PNG_FILE_PATH = sys.argv[2]

WORKSHEET = sys.argv[3]
FIRST_CELL = sys.argv[4]
LAST_CELL = sys.argv[5]

print(f"Excel File Path: {EXCEL_FILE_PATH}")
print(f"Output PNG File Path: {OUTPUT_PNG_FILE_PATH}")
print(f"WORKSHEET: {WORKSHEET}")
print(f"FIRST_CELL: {FIRST_CELL}")
print(f"LAST_CELL: {LAST_CELL}")

print(f"Absolute Excel File Path: {EXCEL_FILE_PATH}")
print(f"Absolute PNG File Path: {OUTPUT_PNG_FILE_PATH}")

try:
    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = False
    wb = o.Workbooks.Open(EXCEL_FILE_PATH)
    worksheet = wb.Worksheets(WORKSHEET)
    used_range = worksheet.Range(FIRST_CELL, LAST_CELL)
    used_range.CopyPicture(Format=2)

    wb.Close(True)

    img = ImageGrab.grabclipboard()
    if img is None:
        print("No image found in clipboard.")
    else:
        # Save the image temporarily
        img.save(OUTPUT_PNG_FILE_PATH, 'PNG')

except Exception as e:
    print('Image Export Failed!')
    raise e
else:
    print('Image Export Succeeded!')