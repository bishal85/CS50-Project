import os
import os.path

from project import docxtopdf
from project import docxtotxt

from project import docxtobook
# get the current working directory
current_working_directory = os.getcwd()

def test_docxtopdf():
    docxtopdf("new1.docx","HELLO1.pdf")
    assert os.path.isfile(current_working_directory+"/HELLO1.pdf")==True
def test_docxtotxt():

    docxtotxt("new1.docx","HELLO.txt")
    assert os.path.isfile(current_working_directory+"/HELLO.txt")==True
def test_docxtobook():


    docxtobook("new1.docx","HELLO.epub")
    assert os.path.isfile(current_working_directory+"/HELLO.epub")==True


