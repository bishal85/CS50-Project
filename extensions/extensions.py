string=input("File name: ")
string=string.strip()
b=string.find('.')
string2=len(string)
a=len(string)-1
if(b!=-1):
    while string[a]!=".":
           a=a-1
    if string[a+1:string2]=="git":
       print("image/git")
    elif string[a+1:string2]=="jpeg":
       print("image/jpeg")
    elif string[a+1:string2]=="jpg":
       print("image/jpeg")
    elif string[a+1:string2]=="png":
       print("image/png")
    elif string[a+1:string2].casefold()== 'pdf':
       print("application/pdf")
    elif string[a+1:string2]=="txt":
       print("text/"+string[0:a])
    elif string[a+1:string2]=="zip":
        print("application/zip")
    elif string[a+1:string2]=="gif":
        print("image/gif")
    else:
        print("application/octet-stream")
else:
  print("application/octet-stream")
