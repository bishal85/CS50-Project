
string2={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
b=1
string5={}
while True:
     try:
         string1=''
         string="E"
         string=input("Date: ")
         if '/' in string:
             a,b,c=string.split("/")
             if int(b)>31 or int(a)>12:
                 continue
             if int(a)<10 and int(b)>=10:
                   print(c+"-0"+a+"-"+b)
                   break
             elif int(a)<10 and int(b)<10:
                   print(c+"-0"+a+"-0"+b)
                   break
             elif int(a)>=10 and int(b)<10:
                   print(c+"-"+a+"-0"+b)
                   break
             else:
                  print(c+"-"+b+"-"+a)
                  break
         elif string[0:2].isalpha()==True:
             d,e,h=string.split(" ")
             k=len(e)-1
             m=int(e[0:k])
             if m>31 or string2[d]>12:
                 continue
             if m<10 and string2[d]>=10:
                   print(h+"-"+str(string2[d])+"-0"+e[0:k])
                   break
             elif m<10 and string2[d]<10:
                   print(h+"-0"+str(string2[d])+"-0"+e[0:k])
                   break
             elif m>=10 and string2[d]<10:
                   print(h+"-0"+str(string2[d])+"-"+e[0:k])
                   break
             else:
                   print(h+"-"+str(string2[d])+"-0"+e[0:k])
                   break

     except EOFError:

         pass
     except ValueError:
         pass
     else:
         pass

