string=input("How much was the meal? ")
string4=input("What percentage would you like to tip? ")
string2=string.replace("$","")
string5=string4.replace("%","")
a=float(string2)
b=float(string5)
tip=float(a*b)/100
print(format(tip, '.2f'))

