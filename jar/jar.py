import csv
import sys
class Jar:
    def __init__(self, capacity=12):
        self.line=line
        self.b1=b1
    def __str__(self):
         self.b1=b1
         return b1

    def deposit(self,n):
        c=0
        n=int(n)
        j="a"
        file1=open("hello.csv", 'r')
        line2=file1.readlines()
        for m in line2:
            c=c+1
        n=c+n
        csvfile=open("hello.csv",'w')
        writer = csv.writer(csvfile)
        while n!=0:
           writer.writerow("a")
           n=n-1
        a1=""
        file=open("hello.csv",'r')
        line=file.readlines()
        for k in line:
             a1=a1+k
        b1=str(a1)
        return f"{n}"
    @classmethod
    def deposit1(self,k):
         j=deposit(k)


def main():
        jar=Jar.deposit(1)
        print(jar)

        a1=""
        file=open("hello.csv",'r')
        line=file.readlines()
        for k in line:
             a1=a1+k
        b1=str(a1)
        print(b1)






if __name__=="__main__":
    main()
