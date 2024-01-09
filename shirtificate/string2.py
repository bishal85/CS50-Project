
import sys
import os
import os.path
from spire.doc import *
from spire.doc.common import *
def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   if ".docx" in j and ".txt" in j2:
      docxtotxt(j,j2)
   elif ".docx" in j and ".pdf" in j2:
      docxtopdf(j,j2)
   elif ".docx" in j and ".epub" in j2:
      ptopdf(j,j2)
def docxtopdf(a2,b2):
   document = Document()
   document.LoadFromFile(a2)
   document.SaveToFile(b2, FileFormat.PDF)
   document.Close()
def docxtotxt(a,b):
   document1 = Document()
   document1.LoadFromFile(a)
   document1.SaveToFile(b, FileFormat.Txt)
   document1.Close()
def docxtobook(a1,b1):
    document1 = Document()
    document1.LoadFromFile(a)
    document1.SaveToFile(b, FileFormat.EPub)
    document1.Close()


if __name__=="__main__":
    main()

