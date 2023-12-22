def main():
   string=input(" ")

   string2=shorten(string)
   print(string2)

def shorten(word):


    string1=''

    for a in word:

        if a.lower()!='a' and a.lower()!='i' and a.lower()!='e' and a.lower()!='o' and a.lower()!='j':
             string1=string1+a
    return string1

if __name__ == "__main__":
    main()
