
import sys
import random
from pyfiglet import Figlet
Figlet = Figlet()

b=len(sys.argv)
def main():
    if b < 2:
        a = random.choice(Figlet.getFonts())
        string1("Input: ", a)
    elif b > 2 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in Figlet.getFonts():
        a= sys.argv[2]
        string1("Input: ", a)
    else:
        sys.exit("Invalid usage")
def string1(input1, m):
    string = input(input1)
    Figlet.setFont(font=m)
    print("Output:")
    print(Figlet.renderText(string))
main()
