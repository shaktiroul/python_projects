import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0        # how many intervals have passed (work + breaks)
timer = None    # will store the after() id so we can cancel it

# ---------------------------- TIMER RESET ----------------------------- #
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # Every 8th rep → long break
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # Every even rep (2, 4, 6) → short break
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # Odd reps (1, 3, 5, 7) → work sessions
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM --------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    # Format as 00:00
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When timer hits 0, start next session
        start_timer()

        # Add checkmarks for completed work sessions
        work_sessions = math.floor(reps / 2)
        marks = "✔" * work_sessions
        checkmarks_label.config(text=marks)

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Replace this with the path to your tomato image if you have one
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmarks_label.grid(column=1, row=3)

window.mainloop()
