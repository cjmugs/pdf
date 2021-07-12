import PyPDF2
import sys

# grabs all of the arguements after the filename
inputs = sys.argv[1:]

def pdf_combine(pdf_list):
    for pdf in pdf_list:
        print(pdf)
        
pdf_combine(inputs)
