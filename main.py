"""
projekt_1.py: první project do Engeto Online Python Akademie
author: Martina Fúsiková
email: martina.fusikova@gmail.com
discord: Martina_F #2319
"""
import re
import collections

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
SYMBOLS = '.,:;'
TEXTS_1 = []
for element in TEXTS:
    temp = ""
    for ch in element:
        if ch not in SYMBOLS:
            temp += ch
    TEXTS_1.append(temp)

# seznam uživatelů
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# pomocne oddelovace
oddelovac_1 = "----------------------------------------"
mezera = " "
hvezda = "*"
# přihlášení
user = input("username: ")
password = input("password: ")

# vyhodnocení uzivatele
if user in users.keys() and password == users.get(user):
    print(
        "", oddelovac_1, "\n",
        "Welcome to the app,", user, "\n",
        "We have 3 texts to be analyzed.", "\n",
        oddelovac_1,
    )
    text_number: str = input("Enter a number btw. 1 and 3 to select: ")
    edit_text_number: int = int(text_number) - 1
    for index, text in (enumerate(TEXTS_1)):
        if edit_text_number == index:
            # numeric string
            result_sum = (re.findall(r"([0-9]+\s)", text))
            # sum of all numbers
            results = list(map(int, result_sum))
            # titlecase words
            titlecase = (re.findall(r"\s([A-Z]\w+)", text))
            # uppercase words
            uppercase = (re.findall(r"([A-Z][A-Z]+)", text))
            # lowercase words
            lowercase = (re.findall(r"\s([a-z]+)", text))
            split_text = (text.split())

            print(
                oddelovac_1, "\n",
                "There are", len(split_text), "words in the selected text.", "\n",
                "There are", len(titlecase), "titlecase words.", "\n",
                "There are", len(uppercase), "uppercase words.", "\n",
                "There are", len(lowercase), "lowercase words", "\n",
                "There are", len(result_sum), "numeric string", "\n",
                "The sum of all the numbers", (sum(results)), "\n",
                oddelovac_1, "\n",
                "LEN|", (3*mezera), "OCCURENCES", (3*mezera), "|NR.", "\n",
                oddelovac_1
            )
            # délka slov
            sum_slovo = []
            for pozice, slovo in enumerate(split_text, 1):
                sum_slovo.append(len(slovo))
            cislovka = range(1, len(sum_slovo))
            cislovka_list = []
            for (cislovka) in sorted(sum_slovo):
                cislovka_list.append(cislovka)
            jednotlive_pocty = collections.Counter(cislovka_list)
            for key, value in sorted(jednotlive_pocty.items()):
                print(f"{key:>3} | {(hvezda * value): <18} | {value}")

            break
    else:
        print("wrong input, terminating the program...")
else:
    print("unregistered user, terminating the program...")
