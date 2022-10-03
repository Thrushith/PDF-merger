import PyPDF2
from PyPDF2 import PdfFileMerger
import sys
import os
merger = PyPDF2.PdfFileMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):       
        merger.append(file)
        merger.write("combinePDF.pdf")
merger.close()