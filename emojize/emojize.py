import emoji
string=input("input ")

c=string.find(", ")
if c!=-1:
    a,b=string.split(", ")
    print("Output: "+a+' '+emoji.emojize(b))
else:
    print("Output: "+emoji.emojize(string, ))
