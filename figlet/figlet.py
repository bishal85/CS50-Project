import sys
from pyfiglet import Figlet

string=input()
figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=sys.argv[1:])

print(figlet.renderText(string))
