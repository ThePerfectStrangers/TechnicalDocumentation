#!/usr/bin/env python3

import sys
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

OUTPUT_FILE_PATH = sys.argv[1]
TITLE = sys.argv[2]
AUTHOR = sys.argv[3]
SUBJECT = sys.argv[4]

print(f"Output Path: {OUTPUT_FILE_PATH}")

pdfs = []

for i in range(5, len(sys.argv)):
    pdfs.append(sys.argv[i])

print(f"PDFs To Combine: {pdfs}")

writer = PdfWriter()
for inpfn in pdfs:
    writer.addpages(PdfReader(inpfn).pages)

writer.trailer.Info = IndirectPdfDict(
    Title=TITLE,
    Author=AUTHOR,
    Subject=SUBJECT,
    Creator=AUTHOR,
)

writer.write(OUTPUT_FILE_PATH)