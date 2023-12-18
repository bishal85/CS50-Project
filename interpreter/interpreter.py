string=input("Expression: ")
j=0
b=string.find('+')
c=string.find('-')
d=string.find('*')
e=string.find('/')
string1=string.replace(" ","")

string2=len(string1)
string1=string1.replace('-','')
string1=string1.replace('+','')
string1=string1.replace('*','')
if b!=-1:
    string1=int(string1)
    while string1>0:
        a=float(string1%10)
        j=j+a
        string1=int(string1/10)
elif c!=-1:
    string1=int(string1)
    while string1>0:
         a=int(string1%10)
         j=int(a-j)
         string1=int(string1/10)

elif d!=-1:
    j=1
    string1=int(string1)
    while string1>0:
         a=int(string1%10)
         j=int(j*a)
         string1=int(string1/10)
elif e!=-1:
    a=0
    while string1[a]!="/":
           a=a+1
    j=1
    string1=string1.replace('/','')
    string3=int(string1[0:a])
    string4=int(string1[a:string2])
    j=float(string3/string4)

print(format(j, '.1f'))
