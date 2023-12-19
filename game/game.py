import random
while True:
    try:
         string1=int(input("Level: "))
         a=random.randint(1,string1)
         while True:
             string=int(input("Guess: "))

             if a==string:
                 print("Just right!")
                 break
             elif a>string:
                 print("Too small!")
             elif a<string:
                 print("Too Large!")
         if a>=0:
             break
    except ValueError:
        pass
    else:
        pass
