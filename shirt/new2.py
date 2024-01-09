from spire.doc import *
from spire.doc.common import *

def docxtopdf(a,b):
# Create a Document object
   document = Document()
# Load a Word DOCX file
   document.LoadFromFile(a)
   document.SaveToFile(b, FileFormat.PDF)
   document.Close()
def pdftodocx(a,b)
