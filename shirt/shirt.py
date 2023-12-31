import os

import sys
from PIL import Image,ImageOps
def main():
    try:
        c=0
        a=''
        b=0
        d="."
        e=sys.argv
        k=str(e)
        m1=''
        n=''
        if len(sys.argv)==3:
            m1,n2,n5=k.split(" ")
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too Many command-line argument")
        else:
            m52=os.path.splitext(sys.argv[1])
            m57=os.path.splitext(sys.argv[2])
            m71=[".jpg",".jpeg",".png"]
            if m57[1] not in m71:
                  if len(e)==3:
                     sys.exit("Invalid Input")
            elif m52[1].lower()!=m57[1].lower():
                  sys.exit("Input and output have different extentions")
            else:
                  print("Empty")
                  string5(sys.argv[1],sys.argv[2])
# Loop through the rest of the file and print each line
    except FileNotFoundError:
           print("Flie does not exits")
    else:
           pass
def string5(input1,output):
    a=str(input1)

    b=str(output)
    shirt = Image.open("shirt.png")
    with Image.open(a) as image:
        image=ImageOps.fit(image,shirt.size)
        image.paste(shirt,mask=shirt)
        image.save(b)
if __name__=="__main__":
   main()

