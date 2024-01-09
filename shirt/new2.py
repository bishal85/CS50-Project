from spire.doc import *
from spire.doc.common import *

from spire.pdf.common import *
from spire.pdf import *
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
# Close the PdfDocument object
   pdf.Close()
