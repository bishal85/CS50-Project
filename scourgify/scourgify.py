
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
     if len(sys.argv)==3:
        m1,n2,n5=k.split(" ")
        print(n2)
        print(n5)
     if len(sys.argv)<3:
         sys.exit("Too few command-line arguments")
     elif len(sys.argv)>3:
         sys.exit("Too Many command-line argument")
     elif d in n2 and len(e)==3:
          m2,n1=n2.split(".")
          m7,n52=n5.split(".")
          print(n1)
          if n1[0:len(n1)-2]!="csv" or n52[0:len(n52)-2]!="csv" :
             sys.exit("Not a csv file")
          elif n1[0:len(n1)-2]=="csv" and  n52[0:len(n52)-2]=="csv":
             if len(sys.argv)==3:
                 print(n1)
                 print(n52)
                 a1=[]
                 b1={}
                 a5=''
                 d2=''
                 csvfile=open(sys.argv[2], 'w', newline='')
                 fieldnames = ['first_name', 'last_name', 'house']
                 writer = csv.writer(csvfile)
                 file=open(sys.argv[1])
                 line=csv.DictReader(file)
                 writer.writerow(["first","last","house"])
                 for n in line:
                      a27,a32=n['name'].split(", ")
                      writer.writerow([a32,a27,n['house']])

     elif d not in sys.argv[1]:
          if d not in sys.argv[2]:
             sys.exit("Not CSV")
          elif len(e)==3:
             sys.exit("Not CSV")
# Loop through the rest of the file and print each line
except FileNotFoundError:
    sys.exit("Could not Read"+str(sys.argv[1]))
else:
     pass
