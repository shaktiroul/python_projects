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

invited_names = []
with open("../Input/Names/invited_names.txt") as names:
    content = names.read()
    for name in names:
        invited_names.append(name)
print(invited_names)
