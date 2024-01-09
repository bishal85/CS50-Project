from spire.doc import *
from spire.doc.common import *

import sys
from spire.pdf.common import *
from spire.pdf import *

from spire.presentation import *
from spire.presentation.common import *
def docxtopdf(a,b):
# Create a Document object
   document = Document()
# Load a Word DOCX file
   document.LoadFromFile(a)
   document.SaveToFile(b, FileFormat.PDF)
   document.Close()
def pdftodocx(a,b):
   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()
def ptopdf(a,b):
   presentation = Presentation()
# Load a PowerPoint presentation in PPTX format
   presentation.LoadFromFile(a)
   presentation.SaveToFile(b, FileFormat.PDF)
   presentation.Dispose()



def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   if ".pdf" in j and ".docx" in j2:
      docxtopdf(j,j2)
   elif ".docx" in j and ".pdf" in j2:
      pdftodocx(j,j2)
   elif ".ppt" in j and ".pdf" in j2:
      ptopdf(j,j2)

if __name__=="__main__":
    main()

