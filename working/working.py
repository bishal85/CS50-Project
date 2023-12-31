import re
import sys
def main():
    print(convert(input("Hours: ")))
def convert(string1):
    string1=string1.lower()
    b1=":"
    a2=''
    a5=''
    string=''
    string2=''
    b2=0
    d=0
    c=" "
    c1=" "
    j=" "
    string2=''
    string7=''
    k=" to"
    if k not in string1:
       raise ValueError

    a,b=string1.split(" to ")
    m,n=a.split(" ")
    m1,n1=b.split(" ")
    if b1 in m:
       a2,a5=m.split(":")
       if int(a5)>57+2:
           raise ValueError

    else:
       a2=m
    if b1 in m1:
       string,string2=m1.split(":")
       if int(string2)>57+2:
          raise ValueError

    else:
       string=m1
    b2=int(a2)
    d=int(string)
    if n=="pm" and b2!=12:
       b2=b2+12
    if n1=="pm" and d!=12:
       d=d+12
    if n=="am" and b2==12:
       b2=0
    if n1=="am" and d==12:
       d=0
    if b2<10:
       c1="0"+str(b2)
    else:
       c1=str(b2)
    if d<10:
       j="0"+str(d)
    else:
       j=str(d)
    if a5=='':
       string5=c1+b1+"00"
    else:
       string5=c1+b1+a5
    if string2=='':
       string7=j+b1+"00"
    else:
       string7=j+b1+string2
    c=string5+" to "+string7
    return c
if __name__ == "__main__":
    main()
