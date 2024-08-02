#!/usr/bin/env python3

import excel2img
import win32com.client
from pywintypes import com_error

EXCEL_FILE_PATH = 'Input List/Full Band/Input List.xlsx'

INPUT_EQUIPMENT_SHEET = 'Input + Equipment'
INPUT_EQUIPMENT_RANGE = '$A$3:$I$35'
PATH_TO_INPUT_EQUIPMENT_PNG = 'Input List/Full Band/Input + Equipment.png'

PATH_TO_PDF = 'Input List/Full Band/Input List.pdf'

excel2img.export_img(EXCEL_FILE_PATH, PATH_TO_INPUT_EQUIPMENT_PNG, INPUT_EQUIPMENT_SHEET, INPUT_EQUIPMENT_RANGE)

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False
try:
    print('Start conversion to PDF')
    # Open
    wb = excel.Workbooks.Open(EXCEL_FILE_PATH)
    # Specify the sheet you want to save by index. 1 is the first (leftmost) sheet.
    ws_index_list = [1,2]
    wb.WorkSheets(ws_index_list).Select()
    # Save
    wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
except com_error as e:
    print('failed.')
else:
    print('Succeeded.')
finally:
    wb.Close()
    excel.Quit()