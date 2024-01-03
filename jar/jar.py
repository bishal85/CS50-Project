import csv
import sys
class Jar:
    def __init__(self, capacity=12):
        self.line=line
        self.n=n


    def deposit(n):
        c=0
        n=int(n)
        j="a"
        file=open("hello.csv", 'r')

        line=file.readlines()
        for m in line:
            c=c+1
        n=c+n
        csvfile=open("hello.csv",'w')

        writer = csv.writer(csvfile)
        while n!=0:
           writer.writerow(j)
           n=n-1
def main():
    jar=Jar.deposit(2)
    a1=[]
    file=open("hello.csv",'r')
    line=csv.DictReader(file)
    for k in line:
            print(k)
    print(a1)

if __name__=="__main__":
    main()
