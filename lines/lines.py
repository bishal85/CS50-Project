import sys
try:
     c=0
     a=''
     b=0
     d="."
     e=sys.argv
     k=str(e)
     m1=''
     n=''
     if len(sys.argv)==2:
        m1,n=k.split(" ")
     if len(sys.argv)==1:
         sys.exit("Too few command-line arguments")
     elif d in n and len(e)==2:
          m2,n1=n.split(".")
          if n1[0:len(n1)-2]!="py":
             sys.exit("Not a Python file")
          elif n1[0:len(n1)-2]=="py":
             if len(sys.argv)==2:
                  file=open(sys.argv[1], 'r')
                  line=file.readlines()
                  for m in line:

                         if m.isspace()==False:
                            m=m.lstrip()
                            if m[0]!='#':

                               c=c+1

          print(str(c))
     elif d not in sys.argv[1]:
          if len(e)==2:
             sys.exit("Not a Python file")
     elif len(sys.argv)>2:
         sys.exit("Too Many command-line argument")
# Loop through the rest of the file and print each line
except FileNotFoundError:
    print("Flie does not exits")
else:
     pass


