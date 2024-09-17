#!/usr/bin/env python3

import sys
import win32com.client
from PIL import ImageGrab
import excel2img

EXCEL_FILE_PATH = sys.argv[1]
OUTPUT_PNG_FILE_PATH = sys.argv[2]

WORKSHEET = sys.argv[3]
RANGE = sys.argv[4]

print(f"Excel File Path: {EXCEL_FILE_PATH}")
print(f"Output PNG File Path: {OUTPUT_PNG_FILE_PATH}")
print(f"WORKSHEET: {WORKSHEET}")
print(f"RANGE: {RANGE}")

print(f"Absolute Excel File Path: {EXCEL_FILE_PATH}")
print(f"Absolute PNG File Path: {OUTPUT_PNG_FILE_PATH}")

try:
    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = False
    wb = o.Workbooks.Open(EXCEL_FILE_PATH)
    worksheet = wb.Worksheets(WORKSHEET)
    used_range = worksheet.UsedRange
    used_range.CopyPicture(Format=2)

    wb.Close(True)

    img = ImageGrab.grabclipboard()
    if img is None:
        print("No image found in clipboard.")
    else:
        # Save the image temporarily
        img.save(OUTPUT_PNG_FILE_PATH, 'PNG')

    OUTPUT_PNG_FILE_PATH2 = OUTPUT_PNG_FILE_PATH + "2"
    excel2img.export_img(EXCEL_FILE_PATH, OUTPUT_PNG_FILE_PATH2, WORKSHEET, RANGE)
    print("Bonus: {OUTPUT_PNG_FILE_PATH2}")


except Exception as e:
    print('Image Export Failed!')
    raise e
else:
    print('Image Export Succeeded!')