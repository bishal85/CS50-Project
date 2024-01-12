import os
import os.path

from Project.project import docxtopdf
from Project.project import docxtotxt

from Project.project import docxtobook
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


