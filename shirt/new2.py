
import sys


def docxtopdf(a,b):
   from spire.doc import *
   from spire.doc.common import *
# Create a Document object
   document = Document()
# Load a Word DOCX file
   document.LoadFromFile(a)
   document.SaveToFile(b, FileFormat.PDF)
   document.Close()
def pdftodocx(a,b):
   from spire.pdf.common import *
   from spire.pdf import *
   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()
def ptopdf(a,b):
   from spire.presentation import *
   from spire.presentation.common import *
   presentation = Presentation()
# Load a PowerPoint presentation in PPTX format
   presentation.LoadFromFile(a)
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

