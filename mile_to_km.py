from tkinter import *

# -------------------- Conversion function -------------------- #
def miles_to_km():
    miles = miles_input.get()
    try:
        miles_value = float(miles)
        km_value = miles_value * 1.60934
        km_result_label.config(text=f"{km_value:.2f}")
    except ValueError:
        km_result_label.config(text="Error")

# ------------------------ UI Setup --------------------------- #
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Entry for miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# "Miles" label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# "is equal to" label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Result label (for km)
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# "Km" label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
