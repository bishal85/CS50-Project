import csv
import sys
class Jar:
    def __init__(self, capacity=12):
        self.line=line
        self.n=n


    def deposit(n):
        n=int(n)
        j="a"
        csvfile=open("hello.csv",'w')

        writer = csv.writer(csvfile)
        while n!=0:
           writer.writerow(j)
           n=n-1
        a1=[]
        file=open("hello.csv")
        line=csv.DictReader(file)
        for k in line:
            a1.append([k])
        return a1
def main():
    a1=[]
    file=open("hello.csv")
    line=csv.DictReader(file)
    for k in line:
            a1.append([k])
    print(a1)

if __name__=="__main__":
    main()
