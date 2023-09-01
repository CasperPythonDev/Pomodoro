import tkinter as tk
from tkinter import Label, Button
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# not a constant, consider refactor
reps = 0
check_marks_list = []

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():  # Alternative to lambda
    global reps
    reps += 1
    # work_timer = WORK_MIN * 60
    # short_b_timer = SHORT_BREAK_MIN * 60
    # long_b_timer = LONG_BREAK_MIN * 60
    work_timer = 5  # Test
    short_b_timer = 2  # Test
    long_b_timer = 10  # Test

    if reps % 8 == 0:
        count_down(long_b_timer)
        print(f"Long break: {reps}")
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        print(f"Short break: {reps}")
        count_down(short_b_timer)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_timer)
        print(f"Work flow: {reps}")
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_remaining = floor(count / 60)
    sec_remaining = count % 60
    global check_marks_list
    if sec_remaining < 10:
        sec_block = f"0{sec_remaining}"
    else:
        sec_block = sec_remaining

    min_block = min_remaining  # Consider same logic as above for min

    timer = f"{min_block}:{sec_block}"
    canvas.itemconfig(canvas_timer, text=timer)

    if count > -1:
        app.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks_list.append("✔")
            check_marks.config(text=check_marks_list)


# ---------------------------- UI SETUP ------------------------------- #
app = tk.Tk()
app.title("Pomodoro")
app.config(padx=100, pady=50, bg=YELLOW)
"""
WIDTH = 500
HEIGHT = 500
window = tk.Tk()

window.title("My first GUI")
window.minsize(width=WIDTH, height=HEIGHT)
"""
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_image = tk.PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=background_image)
canvas_timer = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Labels
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12))
check_marks.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
# lambda function allows us to pass argument with function in TKinter framework. # command=lambda: count_down(5)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)
# - function calls


# - mainloop
app.mainloop()
