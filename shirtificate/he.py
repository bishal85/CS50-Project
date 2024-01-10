from PyPDF2 import PdfMerger
import os

import sys

#Create an instance of PdfFileMerger() class
merger = PdfMerger()

#Define the path to the folder with the PDF files
path_to_files = os.getcwd()
a=1
a1=[]
while len(sys.argv)-1>=a:

    a1.append(str(sys.argv[a]))
    a=a+1


#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_files):
    #Iterate over the list of the file names
    for file_name in a1:
        #Append PDF files
        merger.append(path_to_files +"/"+ file_name)

#Write out the merged PDF file
merger.write(str(sys.argv[len(sys.argv)]))
merger.close()
