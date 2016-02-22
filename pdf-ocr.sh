#!/bin/sh
STARTPAGE=1 # set to pagenumber of the first page of PDF you wish to convert
ENDPAGE=2 # set to pagenumber of the last page of PDF you wish to convert
SOURCE=1-4.pdf # set to the file name of the PDF
OUTPUT=1-4.txt # set to the final output file
RESOLUTION=600 # set to the resolution the scanner used (the higher, the better)

touch $OUTPUT
for i in `seq $STARTPAGE $ENDPAGE`; do
    # convert image.pdf image_%0d.tiff
    convert -monochrome -density $RESOLUTION $SOURCE\[$(($i - 1 ))\] page.tif
    echo processing page $i
    tesseract page.tif tempoutput
    cat tempoutput.txt >> $OUTPUT
done
# rm page.tif
# rm tempoutput.txt

# Not using Pillow, nor ReportLab ---> pypdfocr not working with Python 3
# Not using Rufus, nor Pillow, nor ReportLab --> ocrmypdf
