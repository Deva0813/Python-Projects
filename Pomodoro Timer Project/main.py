from time import sleep
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
reps = 0
time = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    tick.config(text="")
    window.after_cancel(time)
    timer.config(text="TIMER", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        start_count(LONG_BREAK_MIN*60)
        timer.config(text="Long Break", fg=PINK)

    elif reps % 2 == 0:
        start_count(SHORT_BREAK_MIN*60)
        timer.config(text='Break', fg=RED)
    else:
        start_count(WORK_MIN*60)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_count(count):
    global time
    global reps
    count_min = count//60
    count_sec = count % 60

    canvas.itemconfig(
        timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}")
    if count > 0:
        time = window.after(1000, start_count, count-1)
    else:
        start_timer()
        mark = ""
        for i in range(reps//2):
            mark += "✔️"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(
    file=".\tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer.config(bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

tick = Label(fg=GREEN)
tick.config(bg=YELLOW)
tick.grid(column=1, row=3)

window.mainloop()
