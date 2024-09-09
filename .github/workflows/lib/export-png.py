#!/usr/bin/env python3

import sys
import win32com.client
import os
from PIL import ImageGrab

EXCEL_FILE_PATH = sys.argv[1]
INPUT_EQUIPMENT_PNG_PATH = sys.argv[2]

EXCEL_FILE_ABSOLUTE_PATH = os.path.abspath(EXCEL_FILE_PATH)
INPUT_EQUIPMENT_PNG_ABSOLUTE_PATH = os.path.abspath(INPUT_EQUIPMENT_PNG_PATH)

INPUT_EQUIPMENT_SHEET = sys.argv[3]
INPUT_EQUIPMENT_RANGE = sys.argv[4]

try:
    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = False
    wb = o.Workbooks.Open(EXCEL_FILE_ABSOLUTE_PATH)
    worksheet = wb.Worksheets(INPUT_EQUIPMENT_SHEET)
    used_range = worksheet.UsedRange
    used_range.CopyPicture(Format=2)

    wb.Close(True)

    img = ImageGrab.grabclipboard()
    if img is None:
        print("No image found in clipboard.")
    else:
        # Save the image temporarily
        img.save(INPUT_EQUIPMENT_PNG_ABSOLUTE_PATH, 'PNG')

except Exception as e:
    print('Image Export Failed!')
    raise e
else:
    print('Image Export Succeeded!')