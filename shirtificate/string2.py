
import sys
import os
import os.path
from spire.pdf.common import *
from spire.pdf import *
from spire.doc import *
from spire.doc.common import *
def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   if ".pdf" in j and ".docx" in j2:
      pdftodocx(j,j2)
   elif ".docx" in j and ".pdf" in j2:
      docxtopdf(j,j2)
   elif ".ppt" in j and ".pdf" in j2:
      ptopdf(j,j2)
def docxtopdf(a2,b2):

   document = Document()
   document.LoadFromFile(a2)
   document.SaveToFile(b2, FileFormat.PDF)
   document.Close()

def pdftodocx(a,b):
   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()
def ptopdf(a1,b1):
   print(f"{a1}to{b1}")

if __name__=="__main__":
    main()

