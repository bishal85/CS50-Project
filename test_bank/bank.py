import string
def main():

    string=input("Greating: ")
    string=string.strip()
    k=value(string)
    print("$"+str(k))



def value(greeting):
    a=0
    d=0
    e=string.punctuation
    for m in greeting:

         if m==" ":

            break
         else:
            d=d+1
    print(greeting[0:d])
    while any(char in string.punctuation for char in greeting[0:d]):
        d=d-1
    print(greeting[0:d])
    if greeting[0:d].lower()=="hello":
        a=0

    elif greeting[0:d].lower()!="hello" and greeting[0:1].lower()=="h" :
        a=20

    else:
        a=100
    return int(a)



if __name__ == "__main__":
    main()
