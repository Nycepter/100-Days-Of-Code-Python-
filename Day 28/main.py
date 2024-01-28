from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    title_label.config(text="Timer")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(long_break)
        title_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(short_break)
        title_label.config(text="Short Break", fg=RED)
    else:
        countdown(work_time)
        title_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += checkmark
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
checkmark = "✔"
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, ), bg=YELLOW)
title_label.grid(column=1, row=0)


canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomate_image = PhotoImage(file="100-Days-Of-Code-Python-/Day 28/tomato.png")
canvas.create_image(104, 112, image=tomate_image)
timer_text = canvas.create_text(104, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

Reset_button = Button(text="Reset", command=reset_timer)
Reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
