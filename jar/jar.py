import csv
import sys
class Jar:
    def __init__(self, capacity=12):
        self.line=line
        self.n=n

    def __str__(self):
        a1=[]
        file=open("hello.text",'r')
        line=file.readlines()
        for k in line:
            a1.append(k)


    def deposit(n):
        m=int(n)



        j="a"
        csvfile=open("hello.text",'w')

        writer = csv.writer(csvfile)
        while n!=0:
           writer.writerow(j)
           n=n-1



def main():

    jar=Jar.deposit(2)



if __name__=="__main__":
    main()
