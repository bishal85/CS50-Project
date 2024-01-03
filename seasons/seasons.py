from datetime import date
import calendar
import sys
import re
import inflect

import operator
class String1:
        def __init__(self,a2):
            self.a2=a2
        def __str__(self):
            return f"{self.a2}"
        @classmethod
        def get(cls,string):
             try :
                if re.search(r"^(\d{4})\-(\d{2})\-(\d{2})$",string):
                   string7=date.today()
                   d=operator.sub(string7,date.fromisoformat(string))
                   b1=round((d.days)*1440)
                   b2=inflect.engine()
                   a2= b2.number_to_words(b1, andword="")
                   a2=a2.capitalize()
                   return f"{a2} minutes"
                else:
                   sys.exit("Invalid date")
             except ValueError:
                   sys.exit()
def main():
    a1=String1.get(input(" "))
    print(a1)
if __name__ == "__main__":
    main()
