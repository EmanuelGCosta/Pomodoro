from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_time.config(text="Timer", fg=GREEN)
    global marks
    global reps
    reps = 0
    marks = ""

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        label_time.config(text="ESTUDANDO", fg=GREEN)
        count_down(work_sec)
    elif reps in [2, 4, 6]:
        label_time.config(text="PAUSA", fg=PINK)
        count_down(short_break_sec)
    elif reps in [8]:
        label_time.config(text="PAUSA LONGA", fg=RED)
        count_down(long_break_sec)


def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks
        for _ in range(int(reps/2)):
            marks += "✅"
        check_marks.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_time = Label(text="TIMER", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
label_time.grid(column=1, row=0)

button_start = Button(text="Começar", command=start_timer, bg="white", highlightthickness=0)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", bg="white", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()