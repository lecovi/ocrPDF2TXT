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
import argparse  # https://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)
