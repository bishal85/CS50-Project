from spire.pdf.common import *
from spire.pdf import *

import sys
# Create a PdfDocument object
pdf = PdfDocument()
# Load a PDF file
pdf.LoadFromFile(str(sys.argv[1]))

# Convert the PDF file to a Word DOCX file
pdf.SaveToFile(str(sys.argv[2]), FileFormat.DOCX)
# Close the PdfDocument object
pdf.Close()
