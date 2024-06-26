from spire.presentation import Presentation as presentation
from spire.doc import Document as document
import sys
import os

def docxtopdf(a,b):
   document.LoadFromFile(a)
   document.SaveToFile(b, FileFormat.PDF)
   document.Close()
def pdftodocx(a,b):

   print(f"{a}to{b}")


def ptopdf(a,b):
# Load a PowerPoint presentation in PPTX format
   presentation.LoadFromFile(a)
# Or load a PowerPoint presentation in PPT format
#presentation.LoadFromFile("Sample.ppt")

# Convert the presentation to PDF format
   presentation.SaveToFile(b, FileFormat.PDF)
   presentation.Dispose()





def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   if ".pdf" in j and ".docx" in j2:
      docxtopdf(str(sys.argv[1]),str(sys.argv[2]))
   elif ".docx" in j and ".pdf" in j2:
      pdftodocx(j,j2)
   elif ".ppt" in j and ".pdf" in j2:
      ptopdf(j,j2)

if __name__="__main__":
    main()

