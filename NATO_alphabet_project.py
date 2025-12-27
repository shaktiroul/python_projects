# import csv
# with open("nato_phonetic_alphabet.csv") as data:
#     reader = csv.DictReader(data)
#     phonetic_dict = {row["letter"]: row["code"] for row in reader}
# print(phonetic_dict)

#!/usr/bin/env python3
import pandas
# phonetic_dict_pandas = {new_key:new_value for (index, row) in df.iterrows()}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
phonetic_dict_pandas = {row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetic_dict_pandas)
def generate_phonetic():
    User_word = input("Enter a word ").upper()
    try: 
        output_list = [phonetic_dict_pandas[word] for word in User_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()