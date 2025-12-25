from tkinter import *
from random import choice, randint, shuffle

# --------------------- PASSWORD GENERATOR --------------------- #
def generate_password():
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    # Add random letters
    for _ in range(nr_letters):
        password_list.append(choice(letters))

    # Add random symbols
    for _ in range(nr_symbols):
        password_list.append(choice(symbols))

    # Add random numbers
    for _ in range(nr_numbers):
        password_list.append(choice(numbers))

    shuffle(password_list)

    password = "".join(password_list)

    # Clear previous content and insert new password
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # (Optional) Copy to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)

# --------------------------- UI SETUP -------------------------- #
window = Tk()
window.title("Password Generator Example")
window.config(padx=20, pady=20)

# Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=0)

# Entry where password will appear
password_entry = Entry(width=30)
password_entry.grid(column=1, row=0, padx=5)

# Button that triggers the generator
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=0, padx=5)

window.mainloop()
