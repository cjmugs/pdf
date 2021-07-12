import PyPDF2

# This is how to open a file object
with open('C:/Gits/pdf/dummy.pdf', 'rb') as file:
    reader =  PyPDF2.PdfFileReader(file)
    page =  reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('crooked.pdf', 'wb') as new_file:
        writer.write(new_file)
