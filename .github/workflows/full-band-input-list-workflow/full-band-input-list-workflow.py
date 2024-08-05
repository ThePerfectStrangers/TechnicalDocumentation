#!/usr/bin/env python3

import excel2img

EXCEL_FILE_PATH = 'Input List/Full Band/Input List.xlsx'
PATH_TO_INPUT_EQUIPMENT_PNG = 'Input List/Full Band/Input + Equipment.png'

INPUT_EQUIPMENT_SHEET = 'Input + Equipment'

PATH_TO_PDF = 'Input List/Full Band/Input List.pdf'

try:
    excel2img.export_img(EXCEL_FILE_PATH, PATH_TO_INPUT_EQUIPMENT_PNG, None, None)
except:
    print('Image Export Failed!')
else:
    print('Image Export Succeeded!')