from tkinter import *
import math

# 
# --------------------------------- Constants -----------------------------------

WHITE = '#FFFBEB'
BLUE = '#495579'
GREEN = '#06883e'
FONT_NAME = 'Courier'

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
running = False


# --------------------------------- Timer Reset -----------------------------------
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text='00:00')
    # state_label
    state_label.config(text='Timer')
    # reset check marks
    label_filler.config(text='')
    global reps
    reps = 0


# --------------------------------- Timer Mechanism -----------------------------------
def start_timer():
    global running
    if not running:
        running = True
        work_sec = WORK_MIN*60
        short_break_sec = SHORT_BREAK_MIN*60
        long_break_sec = LONG_BREAK_MIN*60

        global reps

        reps += 1

        if reps % 8 == 0:
            
            state_label.config(text='Break. Breathe. Relax.')
            count_down(long_break_sec)
            reps = 0

        elif reps % 2 == 0:
            state_label.config(text='Break. Breathe. Relax.')
            count_down(short_break_sec)

        else:
            state_label.config(text='Focus. Be Grateful.')
            count_down(work_sec)



# --------------------------------- Countdown Mechanism -----------------------------------
def count_down(count):
    min = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f'0{secs}'
    canvas.itemconfig(timer_text, text=f'{min}:{secs}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else: 
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓  "
        label_filler.config(text=marks, fg=GREEN, font=(FONT_NAME, 25), bg=WHITE, pady=20)
        




# --------------------------------- UI Setup -----------------------------------
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=WHITE)

label = Label()
label.config(text='Pomodoro', font=(FONT_NAME, 40, 'bold', 'italic'), fg=GREEN, bg=WHITE, highlightthickness=0)
label.grid(row=0, column=1)

state_label = Label()
state_label.config(text='Timer', font=(FONT_NAME, 20, 'bold'), fg=BLUE, bg=WHITE, highlightthickness=0, pady=20)
state_label.grid(row=1, column=1)


label_filler = Label()
label_filler.config(fg=GREEN, font=(FONT_NAME, 25), bg=WHITE, pady=20)
label_filler.grid(row=3, column=1)

start = Button()
start.config(text='START',font=(FONT_NAME, 10, 'bold'),bg=BLUE, fg=WHITE, padx=10, pady=10, command=start_timer)
start.grid(row=4, column=0)

stop = Button()
stop.config(text='RESET',font=(FONT_NAME, 10, 'bold'),bg=BLUE, fg=WHITE, padx=10, pady=10, command=reset_timer)
stop.grid(row=4, column=2)

canvas = Canvas(width=284, height=300, bg=WHITE, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(142, 150, image=img)
timer_text = canvas.create_text(142, 170, text="00:00", fill=WHITE, font=(FONT_NAME, 40, 'bold'))
canvas.grid(row=2, column=1)


window.mainloop()