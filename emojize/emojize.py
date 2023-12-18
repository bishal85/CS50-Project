import emoji
string=input("input ").strip()

a,b=string.split(" ")
print("Output: "+a+emoji.emojize(b))
