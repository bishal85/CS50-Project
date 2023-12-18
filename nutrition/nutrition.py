
fruits = [{"fruits": "apple", "Calories": "130"},
        {"fruits": "avocado", "Calories": "50"},
        {"fruits": "banana", "Calories": "110"},
        {"fruits": "grapefruit", "Calories": "60"},
        {"fruits": "grapes", "Calories": "90"},
        {"fruits": "honeydew", "Calories": "50"},
        {"fruits": "kiwifruit", "Calories": "90"},
        {"fruits": "lemon", "Calories": "15"},
        {"fruits": "lime", "Calories": "20"},
        {"fruits": "nectarine", "Calories": "60"},
        {"fruits": "orange", "Calories": "80"},
        {"fruits": "peach", "Calories": "60"},
        {"fruits": "pear", "Calories": "100"},
        {"fruits": "pineapple", "Calories": "50"},
        {"fruits": "plums", "Calories": "70"},
        {"fruits": "strawberries", "Calories": "50"},
        {"fruits": "sweet", "Calories": "100"},
        {"fruits": "tangerine", "Calories": "50"},
        {"fruits": "watermelon", "Calories": "80"}]
string=input("Item: ").strip()
string1=string.lower()
string2=''
for a in fruits:
     if a["fruits"] in string1:
         string2=a["Calories"]
         break

print(string2)
