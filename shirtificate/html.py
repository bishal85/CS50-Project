
from spire.doc import Document

import sys
import os

def docxtopdf(a1,b1):
   document=Document()
   document.LoadFromFile(a1)
   document.SaveToFile(b1, FileFormat.PDF)
   document.Close()
def pdftodocx(a,b):

   print(f"{a}to{b}")


def ptopdf(a,b):
# Load a PowerPoint presentation in PPTX format
   presentation.LoadFromFile(a)

   presentation.SaveToFile(b, FileFormat.PDF)
   presentation.Dispose()

def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   if ".docx" in j and ".pdf" in j2:
      docxtopdf(j,j2)
   elif ".pdf" in j and ".docx" in j2:
      pdftodocx(j,j2)
   elif ".ppt" in j and ".pdf" in j2:
      ptopdf(j,j2)

if __name__=="__main__":
    main()

