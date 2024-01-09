import os
import os.path

from string2 import docxtopdf
# get the current working directory
current_working_directory = os.getcwd()

def test_pdf():
    path =current_working_directory+"new2.pdf"

docxtopdf("new1.docx","new2.pdf")
assert  os.path.isfile(current_working_directory+"new2.pdf")=True
