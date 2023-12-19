string2=''
while True:
    try:
        string=input("")
        string2=string2+string+" "
    except EOFError:
        string2=string2.strip()
        break
    else:
        pass
string1=''
c=0
m=0
for b in string2:
    if b==" ":
        c=c+1
for a in string2:
    if a==" ":
        m=m+1
        if m!=c:
             string1=string1+', '
        elif m==c:
             string1=string1+", and "
             c=0
    else:
        string1=string1+a
print("Adieu, adieu, to "+string1)
