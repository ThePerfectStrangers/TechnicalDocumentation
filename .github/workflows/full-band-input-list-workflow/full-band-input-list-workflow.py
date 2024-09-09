#!/usr/bin/env python3

import win32com.client
import excel2img

EXCEL_FILE_PATH = 'Input List/Full Band/Input List.xlsx'

INPUT_EQUIPMENT_SHEET = 'Input + Equipment'
INPUT_EQUIPMENT_RANGE = '$A$3:$I$35'
PATH_TO_INPUT_EQUIPMENT_PNG = 'Input List/Full Band/Input + Equipment.png'

PATH_TO_PDF = 'Input List/Full Band/Input List.pdf'

try:
    excel2img.export_img(EXCEL_FILE_PATH, PATH_TO_INPUT_EQUIPMENT_PNG, INPUT_EQUIPMENT_SHEET, None)
except:
    print('Image Export Failed!')
else:
    print('Image Export Succeeded!')

try:
    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = False
    wb = o.Workbooks.Open(EXCEL_FILE_PATH)
    wb.ExportAsFixedFormat(0, PATH_TO_PDF)
    wb.Close(True)
except:
    print('PDF Export Failed!')
else:
    print('PDF Export Succeeded!')