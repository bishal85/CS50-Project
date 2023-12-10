string=input("M: ")
string=string.replace(":",".")
string=float(string)
if string>=7:
    if string<=9:
        print("breakfast")
if string>=12:
    if string<=13:
        print("lunch")
if string>=18:
    if string<=19:
        print("dinner")
