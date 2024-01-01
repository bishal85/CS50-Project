import validators


def main():
    print(string1(input("What's your email address? ")))
def string1(string):
    if validators.email(string)==True:
        return f"Valid"
    else:
        return f"Invalid"
if __name__=="__main__":
   main()

