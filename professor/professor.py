import random
def main():
    b=0
    c=0
    a=get_level()
    while c!=10:
        print(c)
        string1=''
        e=1
        x=generate_integer(a)
        y=generate_integer(a)
        x1=x
        y1=y
        m=x1+y1
        print(str(x1)+'+'+str(y1), end="")
        string1=input(":")
        if string1.isdigit()==True and m==int(string1):
                b=b+1
                c=c+1
        else:
             print("EEE")
             while e!=3:
                try:
                     print(str(x1)+'+'+str(y1), end="")
                     string1=int(input(""))
                     if string1==m:
                         b=b+1
                         c=c+1
                         break
                     elif string1!=m:
                         print("EEE")
                         e=e+1
                     elif e==3:
                         break
                except ValueError:
                     print("EEE")
                     e=e+1
                else:
                     pass
             if e==3:
                print(str(x1)+'+'+str(y1)+str(m))
                c=c+1
        if c>=10:
            break
    print("Score",b)
def get_level():
    string=''
    while True:
        try:

            string=int(input(""))
            if string==1 or string==2 or string==3:
                     break
        except ValueError:
            pass
        else:
            pass
    return string
def generate_integer(level):
    k=0
    if level==1:
         k=random.randint(0,10-1)
    elif level==2:
         k=random.randint(10,100-1)
    elif level==3:
         k=random.randint(100,1000-1)
    return k
if __name__ == "__main__":
    main()


