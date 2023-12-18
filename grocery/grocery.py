string2={}
b=1
string5={}
while True:
     try:
         string1=''

         string="E"



         string=input("").upper()



         if string in string2:
             string2[string]=string2[string]+1

         else:
             string2[string]=1

     except EOFError:
         string5 = dict(sorted(string2.items()))
         for m in string5:
             print(str(string5[m])+" "+m)
         break
     else:
         pass
