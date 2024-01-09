from spire.pdf.common import *
from spire.pdf import *
from spire.doc import *
from spire.doc.common import *
from spire.presentation import *
from spire.presentation.common import *
import sys
# Create a PdfDocument object
def docxtopdf(a1,b1):
# Create a Document object
   document = Document()
# Load a Word DOCX file
   document.LoadFromFile(a1)
   document.SaveToFile(b1, FileFormat.PDF)
   document.Close()
def pdftodocx(a,b):
   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()
def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])

   if ".docx" in j and ".pdf" in j2:
      pdftodocx(j,j2)


main()
