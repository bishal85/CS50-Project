import os
import os.path

from string2 import docxtopdf
from string2 import docxtotxt
# get the current working directory
current_working_directory = os.getcwd()

def test_pdf():

    docxtopdf("new1.docx","HELLO1.pdf")
    assert os.path.isfile(current_working_directory+"/HELLO1.pdf")==True
def test_text():

    docxtotxt("new1.docx","HELLO.txt")
    assert os.path.isfile(current_working_directory+"/HELLO.txt")==True
def test_

