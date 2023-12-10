string=input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
string1='Forty two'
string2='forty-two'
string=string.strip()
if string.casefold() == '42':
    print("Yes")
elif string.casefold() ==string1.casefold() :
    print("Yes")
elif string==string2.casefold():
    print("Yes")
else:
    print("No")
