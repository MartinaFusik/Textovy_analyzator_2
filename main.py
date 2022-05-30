"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martina Fúsiková
email: martina.fusikova@gmail.com
discord: Martina_F #2319
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

# seznam uživatelů
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# pomoc
oddelovac_1 = "----------------------------------------"
import re
# přihlášení
user = input("username: ")
password = input("password: ")

#vyhodnocení uzivatele
if user in users.keys() and password in users.get(user):
    print(
        "", oddelovac_1, "\n",
        "Welcome to the app,", user, "\n",
        "We have 3 texts to be analyzed.", "\n",
        oddelovac_1,
    )
    text_number: str = input("Enter a number btw. 1 and 3 to selecst: ")
    edit_text_number: int = int(text_number) - 1
    for index, text in (enumerate(TEXTS)):
        if edit_text_number == index:
            print(
            oddelovac_1, "\n",
            "There are", len(text.split()), "words in the selected text.", "\n",
            "There are", len(re.findall(r'\s([A-Z]\w+)', text)), "titlecase words.", "\n",
            "There are", len(re.findall(r'([A-Z][A-Z]+)', text)), "uppercase words.", "\n",
            "There are",
            )
            break
    else:
        print("wrong input, terminating the program...")
else:
    print("unregistered user, terminating the program...")
