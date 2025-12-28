# 1. Aang
# 2. Zuko
# 3. Appa
# 4. Katara
# 5. Sokka
# 6. Momo
# 7. Uncle Iroh
# 8. Toph

# starting_letter.txt in Main/Input/Letters
# invited_names.txt in Main/Input/Names
# output to be stored in Main/Output/ReadytoSend/letter_for_{name.txt}

# """Dear Aang,
# You are invited to my birthday this Sunday.
# Hope you can make it.
# Angela"""

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letters:
            completed_letters.write(new_letter)

