string1=0
string="E"
while True:
     try:
         string2={
         "baja taco": 4.25,
         "burrito": 7.50,
         "bowl": 8.50,
         "nachos": 11.00,
         "quesadilla": 8.50,
         "super burrito": 8.50,
         "super quesadilla": 9.50,
         "taco": 3.00,
         "tortilla salad": 8.00
         }
         string=input("Item: ").lower()
         if not string in string2:
             continue
     except EOFError:
        break
     else:
         string1=string1+string2[string]
         print('$'+str(format(string1,'.2f')))
