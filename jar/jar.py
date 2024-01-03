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
           writer.writerow("a")
           n=n-1
    def func(value):
           return ''.join(value.splitlines())
def main():

    a1=[]
    file=open("hello.csv",'r')
    line=file.readlines()
    for k in line:
            a1.append([k])
    
    print(a1)

if __name__=="__main__":
    main()
