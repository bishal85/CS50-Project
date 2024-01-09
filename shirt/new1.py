import os
import os.path

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)


path ='/workspaces/143246886/shirt'

check_file = os.path.isfile(path)

print(check_file)
from pdf2docx import Converter

pdf_file = '/path/to/sample.pdf'
docx_file = 'path/to/sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
# output

# True
