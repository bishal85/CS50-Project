import re
import sys
def main():
    print(validate(input("IPv4 Address: ")))
def validate(string1):
     k=""
     d=""
     b="Valid"
     b1="Invalid"
     a1=re.search(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",string1)
     if a1:
        m=int(a1.group(1))
        m1=int(a1.group(2))
        n=int(a1.group(3))
        d=int(a1.group(4))
        if m<=255 and n<=255 and m1<=255 and d<=255:
            return True
        else:
            return False
     else:
         return False
if __name__ == "__main__":
    main()
