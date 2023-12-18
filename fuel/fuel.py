
while True:
    try:
        string=input("Fraction: ")
        j=0
        string=string.strip()
        c,d=string.split("/")
        c=int(c)
        d=int(d)
        j=1
        if d==0:
            continue
        else:
            j=float(c/d)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        j=round(float(j*100))
        if 99<=j<=100:
           print("F")
           break
        elif j<=1:
            print("E")
            break
        elif j<100:
            print(str(j)+'%')
            break
        else:
            pass
