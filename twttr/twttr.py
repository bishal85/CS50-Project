string=input(" ")
string1=''
for a in string:
    print(a)
    if a.lower()!='a' and a.lower()!='i' and a.lower()!='e' and a.lower()!='o' and a.lower()!='u':
       string1=string1+a
print(string1)
 