from tkinter import *

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 20, "bold")
WORKING_MIN = 5*60
SHORT_MIN_BREAK = 1*60
LONG_MIN_BREAK = 5*60
timer = None

window = Tk()
window.title("Pomodoro")
# window.geometry("800x800")

canvas = Canvas(width=300, height=250, bg="#EADBC8", highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(150, 125, image=img)
canvas.grid(row=1, column=0, columnspan=9)

time_text = canvas.create_text(150, 150, text="00:00", font=FONT, fill="#CBFFA9")
label = Label(text="Timer", font=FONT, bg="#FAF2D3", fg="#053B50")
label.grid(row=0, column=0, columnspan=9)


def stop_timer():
    global timer
    window.after_cancel(timer)
    greenText.config(text="Start")


def reset_timer():
    global rest_cycle, work_cycle
    if timer is not None:
        window.after_cancel(timer)
    rest_cycle = -1
    work_cycle = -1
    label.config(font=FONT)
    redButton.grid(row=2, column=0, columnspan=3)
    redText.grid(row=2, column=0, columnspan=3)
    greenText.config(text="Reset")
    label.config(text=f"Work Cycle {work_cycle + 2}")
    count_down(WORKING_MIN, 1)


redBtn = PhotoImage(file="redBtn.png")
greenBtn = PhotoImage(file="greenBtn.png")

redButton = Button(text="STOP", height=50, width=180, bg="#FAF2D3", highlightthickness=0,
                   highlightbackground="#FAF2D3", image=redBtn, command=stop_timer)
greenButton = Button(image=greenBtn, bg="#FAF2D3", height=50, highlightthickness=0,
                     highlightbackground="#FAF2D3", command=reset_timer)

redText = Label(text="Stop", fg="#FAF2D3", bg="#FE0000", font=("Arial", 15, "bold"), padx=20)
greenText = Label(text="Start", fg="#FAF2D3", bg="#8EAC50", font=("Arial", 15, "bold"))

# redButton.grid(row=2, column=0, columnspan=3)
greenButton.grid(row=2, column=6, columnspan=3)

# redText.grid(row=2, column=0, columnspan=3)
greenText.grid(row=2, column=6, columnspan=3)

checks = []
for i in range(5):
    checks.append(Label(text="✔", bg="#FAF2D3"))
# Now everytime we are done with one cycle of pomodoro we will display one checkmark

# for i in range(5):
#     checks[i].place(x=103+i*40, y=390, anchor=CENTER)


# Next we need a looping mechanism for the counter; However if we create a while loop
# It wont be able to listen to the onscreen events while the counter is going down

''' so we use window.after() method that takes 3 arguments - time to wait for, function to call after and then *args'''

work_cycle = -1
rest_cycle = -1


def count_down(count, state):
    global work_cycle, rest_cycle, timer, checks

    minute = count // 60
    sec = count % 60
    if minute < 10:
        minute = f"0{minute}"
    if sec < 10:
        sec = f"0{sec}"
    timer = f"{minute}:{sec}"
    canvas.itemconfig(time_text, text=timer)

    if count == 0:
        if state == 1:
            work_cycle += 1
            state *= -1
            checks[work_cycle].place(x=95+work_cycle*40, y=350)
            if work_cycle == 4:
                label.config(text=f"Long Break!!!")
                timer = window.after(0, count_down, LONG_MIN_BREAK, state)
            else:
                label.config(text=f"Break Cycle {rest_cycle + 2}!!!")
                timer = window.after(0, count_down, SHORT_MIN_BREAK, state)

        else:
            rest_cycle += 1
            state *= -1
            if work_cycle == 4:
                label.config(text=f"CONGRATS YOU\nFINISHED ONE CYCLE!", font=FONT)
                greenText.config(text="Start")
                for t in checks:
                    t.place_forget()
            else:
                label.config(text=f"Working Cycle {work_cycle + 2}")
                timer = window.after(0, count_down, WORKING_MIN, state)
    else:
        timer = window.after(1000, count_down, count - 1, state)


window.config(padx=100, pady=50, bg="#FAF2D3")
window.mainloop()
