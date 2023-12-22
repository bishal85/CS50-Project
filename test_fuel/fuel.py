def main():
     string=input("Fraction: ")
     b=convert(string)
     c=gauge(b)
     print(c)

def convert(fraction):
             j=0
             fraction=fraction.strip()
             c,d=fraction.split("/")
             c=int(c)
             d=int(d)
             j=1
             if d==0:
                 raise ZeroDivisionError
             elif c/d>1:
                 raise ValueError
             j=float(c/d)
             j=round(float(j*100))
             return int(j)
def gauge(percentage):
    a=''
    if 99 <= percentage <= 100:
        a="F"

    elif percentage<=1:
        a="E"

    elif percentage<100:
        a=str(percentage)+'%'

    else:
        pass
    return a
if __name__ == "__main__":
    main()
