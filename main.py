import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

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
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()


#
app.mainloop()
