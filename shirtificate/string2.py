from docx2pdf import convert
import sys
import os
import os.path
from spire.pdf.common import *
from spire.pdf import *
def docxtopdf(a,b):
   current_working_directory = os.getcwd()
   print(current_working_directory)
   path1 =current_working_directory+a
   path2=current_working_directory+b
   convert(a,b)

def pdftodocx(a,b):
   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()




def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   docxtopdf(j,j2)
if __name__=="__main__":
    main()

