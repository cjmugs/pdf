import PyPDF2

# This is how to open a file object
with open('C:/Gits/pdf/dummy.pdf', 'rb') as file:
    reader =  PyPDF2.PdfFileReader(file)
    print(reader.numPages)