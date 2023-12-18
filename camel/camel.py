def main():
    string=input("camelcase: ")
    a=0
    while a<len(string):
         if string[a:a+1]==string[a:a+1].upper():
            string1=string[a:a+1].lower()
            string=string[:a]+'_'+string1+string[a+1:]
            a=a+1
         else:
             a=a+1
    print("snakecase: "+string)
main()

