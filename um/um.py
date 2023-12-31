
import re
import sys
def main():
    print(count(input("Text: ")))
def count(string1):
    string1=string1.lower()
    string1=string1.strip()
    a1="um"
    a=0
    b=0
    c=0
    while a<len(string1):
         if b>len(string1):
            sys.exit()
         if a1 in string1[a:a+2]:
            b=a
            if a==0:
               if b+4<=len(string1):
                  b=b+4
                  if re.search(r"um(\W|_| |)+",string1[a:b]):
                     c=c+1
                     a=a+2
                  else:
                     a=a+1
               elif b+4>len(string1):
                    b=len(string1)
                    if re.search(r"um(\W|_| |)+",string1[a:b]):
                        c=c+1
                        break
                    else:
                        a=a+1
            elif a>0:
                 if b+3<=len(string1):
                    b=b+3
                 if b+3>len(string1):
                    b=len(string1)
                 if re.search(r"^um(\W|_| )+",string1[a-1:b]):
                    a=a+2
                    c=c+1
                 elif re.search(r"(\W|_| )+um(\W|_| )+",string1[a-1:b]):
                    a=a+2
                    c=c+1
                 elif re.search(r"(\w)*(\W|_| )+um$",string1[a-1:b]):
                    a=a+2
                    c=c+1
                 else:
                    a=a+1
            else:
                 a=a+1
         else:
            a=a+1
    return c
if __name__ == "__main__":
    main()
