from docx2pdf import convert
import sys
import os

def docxtopdf(a,b):
   convert(a, b)
def pdftodocx(a,b):

   pdf = PdfDocument()
   pdf.LoadFromFile(a)
   pdf.SaveToFile(b, FileFormat.DOCX)
   pdf.Close()
def ptopdf(a,b):

  



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

