
import sys
import tabulate
import csv
try:
     c=0
     a=''
     b=0
     a2=0
     d="."
     e=sys.argv
     k=str(e)
     a2=k.find("sicilian.csv")
     print(a2)
     m1=''
     n=''
     if len(sys.argv)==2:
        m1,n=k.split(" ")
     if len(sys.argv)==1:
         sys.exit("Too few command-line arguments")
     elif d in n and len(e)==2:
          m2,n1=n.split(".")
          print(m2)
          if n1[0:len(n1)-2]!="csv":
             sys.exit("Not a Python file")
          elif n1[0:len(n1)-2]=="csv":
             if len(sys.argv)==2:
                 a1=[]
                 b1={}
                 a5=''
                 d2=''
                 file=open(sys.argv[1])
                 line=csv.DictReader(file)
                     for m in line:
                         a5,d2=m['name'].split(", ")
                         a1.append([a5,,m['Large']])

                     print(tabulate.tabulate(a1,headers=["Regular Pizza","Small","Large"],tablefmt="grid"))

     elif d not in sys.argv[1]:
          if len(e)==2:
             sys.exit("Not a Python file")
     elif len(sys.argv)>2:
         sys.exit("Too Many command-line argument")
# Loop through the rest of the file and print each line
except FileNotFoundError:
    sys.exit("Flie does not exits")
else:
     pass
