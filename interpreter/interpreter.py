string=input("Expression: ")
j=0
b=string.find('+')
c=string.find('-')
d=string.find('*')
e=string.find('/')
if b==1:
    string1=string.replace('+','')
    string1=int(string1.strip())
    while string1>0:
        a=int(string1%10)
        j=float(j+a)
        string1=int(string1/10)
elif c==1:
    string1=string.replace('-','')
    string1=int(string1.strip())
    while string1>0:
         a=int(string1%10)
         j=float(a-j)
         string1=int(string1/10)
         if string1==0:
             break
elif d==1:
    string1=string.replace('*','')
    j=1
    string1=int(string1.strip())
    while string1>0:

         a=int(string1%10)
         j=float(j*a)
         string1=int(string1/10)
elif e==1:
    string1=string.replace('/','')
    j=1
    string1=int(string1.strip())
    while string1>0:

         a=int(string1%10)
         j=float(a/j)
         string1=int(string1/10)
print(format(j, '.1f'))
