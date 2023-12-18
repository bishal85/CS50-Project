import sys
from pyfiglet import Figlet

string=input()
figlet = Figlet()
f=sys.argv[1:]
print(f)
figlet.setFont(font=f)

print(figlet.renderText(string))
