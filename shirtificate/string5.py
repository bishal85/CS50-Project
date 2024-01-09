from spire.pdf.common import *
from spire.pdf import *

import sys
# Create a PdfDocument object

def pdftodocx(a,b):
   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()
def main():
   j=str(sys.argv[1])
   j2=str(sys.argv[2])
   if ".pdf" in j and ".docx" in j2:
      pdftodocx(j,j2)
      


main()
