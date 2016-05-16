#!/usr/bin/env python
# coding: utf-8
"""
    ocrPDF2TXT
    ~~~~~~~~~~

    This is the main module for OCR scanned multipage PDF to TXT files.

    :copyright: (c) 2016 by Leandro E. Colombo Viña.
    :author: Leandro E. Colombo Viña <colomboleandro at bitson.com.ar>.
    :license: GPL v3.0, see LICENSE for more details.

"""
# Standard Lib imports
import argparse
import os
# Third-party imports
import pyPdf

BASEDIR = os.path.abspath(os.path.dirname(__file__))
print(BASEDIR)

parser = argparse.ArgumentParser(
    description="CLI utility to convert scanned multipage PDF to TXT files")

parser.add_argument('input', metavar='in-file',
                    type=argparse.FileType('rb'))
parser.add_argument("-p", action='append', dest='pages_list', default=[],
                    help="Pages to convert",
                    )
# parser.add_argument('-o', metavar='out-file', type=argparse.FileType('wt'))
parser.add_argument("-o", "--output-file",
                    action='store',
                    dest='output_filename',
                    help="Output filename",
                    )
parser.add_argument("-r", "--resolution",
                    action="store",
                    default=600,
                    dest="resolution",
                    type=int,
                    help="set to the resolution the scanner used (the higher, the better)"
                    )

args = parser.parse_args()
#pdf_name = os.path.splitext(os.path.basename(args.input.name))[0]

if not args.pages_list:
    print("No pages list provided, counting PDF pages.")
    pdf_file = pyPdf.PdfFileReader(args.input)
    pdf_pages = pdf_file.getNumPages()

    for page in range(pdf_pages):
        args.pages_list.append(page)

for page in args.pages_list:
    print("Converting page {page_number} to TIFF...".format(page_number=page), end="")
    print("...", end="")
    print("...", end="")
    cmd = "convert -monochrome -density {resolution} {source}[{page_number}] {source}_page[{page_number}].tif".format(
        resolution=args.resolution,
        source=args.input.name,
        page_number=page,
    )
    print("...", end="")
    os.system(cmd)
    print("...", end="")
    print("Ready!")

print()
print("="*80)
print("Now if you want you I'll wait that you edit the TIFF files to get better results with OCR...")
print("="*80)
input("Press <ENTER> when you are ready")

for page in args.pages_list:
    print("Processing page {page_number}...".format(page_number=page), end="")
    print("...", end="")
    print("...", end="")
    cmd = "tesseract {source}_page[{page_number}].tif {source}_page[{page_number}]".format(
        source=args.input.name,
        page_number=page,
    )
    print("...", end="")
    os.system(cmd)
    print("...", end="")
    print("Ready!")
