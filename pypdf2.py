#!/usr/bin/env python3
'''Parse pdf file'''
from PyPDF2 import PdfReader

with open('cv.pdf', 'rb') as f:
    reader = PdfReader(f)
    information = reader.metadata
    pages = len(reader.pages)
    content = ''

    for p in reader.pages:
        content += p.extract_text()
print(content)
