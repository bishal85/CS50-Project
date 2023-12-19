import requests
import json
import sys

try:

    string2=float(input())
    string=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    string1=string.json()
    a=string1["bpi"]["USD"]["rate_float"]
    print(string*a)



except requests.RequestException:
    pass
else:
    pass
