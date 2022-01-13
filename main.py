import tkinter as tk
from tkinter import *
import random
import os

win = tk.Tk()
win.configure(bg="coral")
win.geometry("650x550")
bg_image = PhotoImage(file ="back.png")
x = Label (image = bg_image)
x.grid(row = 650, column = 650)
win.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1 = IntVar()
choice = IntVar()
no = random.randint(1, 99)
result.set("Guess a number between 1 to 99 ")
chances.set(4)
chances1.set(chances.get())


def fun():
    chances1.set(chances.get())
    if chances.get() > 0:

        if choice.get() > 99 or choice.get() < 0:
            result.set("You just lost 1 Chance")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif no == choice.get():
            result.set("Congratulation YOU WON!!!")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif no > choice.get():
            result.set("Your guess was too low: Guess a number higher ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
        elif no < choice.get():
            result.set(
                "Your guess was too High: Guess a number Lower ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
    else:
        result.set(
            "Game Over You Lost")


def restart():
    no = random.randint(1, 99)
    result.set("Guess a number between 1 to 99 ")
    chances.set(5)
    chances1.set(chances.get())


ent1 = Entry(win, textvariable=choice, width=3,
             font=('Algerian', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(win, textvariable=result, width=50,
             font=('Algerian', 15), relief=GROOVE)
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(win, text=chances1, width=2,
             font=('Algerian', 24), relief=GROOVE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(win, text='Number Guessing Game ',
            font=("Algerian", 28,"italic"), relief=GROOVE)
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Remaninig Chances',
             font=("Algerian", 24,"italic"), relief=GROOVE)
msg2.place(relx=0.4, rely=0.85, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=(
    'Algerian', 25,"italic"), command=fun, relief=GROOVE)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = tk.Button(win, text='stop',font=("Bold", 12), width=40, command=win.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=0.98, anchor=S)

reset = tk.Button(win, text='Restart',font=("Bold", 12), width=40, command=restart,
                  bg="red", activebackground="red", relief=GROOVE)
reset.place(relx=0.75, rely=0.98, anchor=S)



win.mainloop()
