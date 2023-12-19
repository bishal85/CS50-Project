import requests
import json
import sys

try:
    c=0
    string4=''
    string2=float(sys.argv[1])
    string=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    string1=string.json()
    a=str(float(string1["bpi"]["USD"]["rate_float"])*string2)
    m,n=a.split(".")
    for k in m:

          c=c+1
          if c%3==0:
               string4=string4+","+k
               c=0
          else:
               string4=string4+k




    print(string4+"."+n)



except requests.RequestException:
    print("Command-Line-argument-is n)
else:
    pass
