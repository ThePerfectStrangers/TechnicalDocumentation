#!/usr/bin/env python3

import win32com.client
import os
from PIL import ImageGrab

EXCEL_FILE_PATH = '../../../Input List/Full Band/Input List.xlsx'
INPUT_EQUIPMENT_PNG_PATH = '../../../Input List/Full Band/Input + Equipment.png'
PDF_FILE_PATH = '../../../Input List/Full Band/Input List.pdf'

EXCEL_FILE_ABSOLUTE_PATH = os.path.abspath(EXCEL_FILE_PATH)
INPUT_EQUIPMENT_PNG_ABSOLUTE_PATH = os.path.abspath(INPUT_EQUIPMENT_PNG_PATH)
PDF_FILE_ABSOLUTE_PATH = os.path.abspath(PDF_FILE_PATH)

INPUT_EQUIPMENT_SHEET = 'Input + Equipment'
INPUT_EQUIPMENT_RANGE = '$A$3:$I$35'

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