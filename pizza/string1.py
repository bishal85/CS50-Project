
import sys

import tabulate
import csv
a1=[]
b1={}
a2="Regular Pizza"
file=open(sys.argv[1])
line=csv.DictReader(file)
for m in line:
    a1.append([m['Regular Pizza'],m['Small'],m['Large']])

print(tabulate.tabulate(a1,headers=[a2,"Small","Large"],tablefmt="grid"))
