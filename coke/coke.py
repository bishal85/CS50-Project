string=50
while string!=0 and string>0:

    print("Amount Due: "+str(string))
    string5=int(input("Insert Coin: "))
    if string5==5 or  string5==10 or  string5==25 or string5==50:
         string=string-string5
    elif string5>50:
         continue
string2=str(string)
string2=string2.replace("-","")
print("Change Owed: "+string2)
