import csv
import sys
class Jar:
    def __init__(self, capacity=12):
        self.line=line
        self.b1=b1
    def __str__(self):
         self.b1=b1
         return b1
    @classmethod
    def deposit(self,n):
        c=0
        n=int(n)
        j="a"
        file1=open("hello.csv", 'r')
        line=file1.readlines()
        for m in line:
            c=c+1
        n=c+n
        csvfile=open("hello.csv",'w')
        writer = csv.writer(csvfile)
        while n!=0:
           writer.writerow("a")
           n=n-1
        a1=[]
        file=open("hello.csv",'r')
        line=file.readlines()
        for k in line:
            a1.append(k)
        b1=str(a1)
        return f"{b1}"

def main():
    jar=Jar.deposit("1")
    print(jar)





if __name__=="__main__":
    main()
