def main():
    plate = input("Plate: ")#if condition is true print valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")#if conditon is false print invalid
def is_valid(string): #returns True or False value
    a=True
    b=0
    c=len(string)
    e=0
    while a:
        if 2<=c<=6 and string.isalnum():
             if len(string)==2 and not string.isalpha():
                 a=False
                 break
             else:
                 for m in string:
                     if m.isdigit():
                         b=b+1
                 if string[-b].isdigit()==True and string[:-b].isdigit()==False and string[-b]!='0':
                     a=True
                     break
                 elif string[-b]=='0':
                     a=False
                     break
                 elif string.isalpha()==True:
                     a=True
                     break
                 else:
                     a=False
                     break
        else:
             a=False
             break
    return a
main()
