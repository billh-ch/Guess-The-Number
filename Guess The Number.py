import tkinter
from tkinter import *
import random
import time

win = tkinter.Tk()
win.title("Guess The Number")
win.geometry("360x300")
win.iconbitmap("dice.ico")

win.resizable(False, False)

up = PhotoImage(file="up.png")
down = PhotoImage(file="down.png")
dice = PhotoImage(file="dice.png")
check = PhotoImage(file="check.png")

number = 0
tries = 0
dif = 0
tried = []
show = False


def entercommand(*args):
    global imagelbl
    global guessentry
    global randomizebtn
    global tries
    global tried
    guess = guessentry.get()
    tried.append(guess)

    status.configure(text="")

    if guess.isdecimal():
        if int(guess) < dif:
            if int(guess) > number:
                imagelbl.configure(image=down)
                tries += 1
            elif int(guess) < number:
                imagelbl.configure(image=up)
                tries += 1
            else:
                imagelbl.configure(image=check)
                guessentry.configure(state="disabled")
                randomizebtn.configure(state="normal", bg="#16C1D4")
                tried.clear()
        else:
            status.configure(text="The guessed number is out of the range you have selected!")
    else:
        pass

    if tries < 10:
        trieslbl.configure(fg="green")
    if 6 <= tries <= 10:
        trieslbl.configure(fg="#FFAE42")
    if tries >= 10:
        trieslbl.configure(fg="red")

    trieslbl.configure(text=tries)
    guessentry.delete(0, END)


def rannum():
    global number
    global difval
    global guessentry
    global randomizebtn
    global dif
    global tries

    print("randomizing")

    guessentry.configure(state="normal")
    randomizebtn.configure(state="disabled", bg="gray")

    if difval.get() == 1:
        temprannum = random.randint(0, 50)
        number = temprannum
        dif = 50
        print(number)

    elif difval.get() == 2:
        temprannum = random.randint(0, 100)
        number = temprannum
        dif = 100
        print(number)
    elif difval.get() == 3:
        temprannum = random.randint(0, 200)
        number = temprannum
        dif = 200
        print(number)

    tries = 0
    trieslbl.configure(text=tries)
    trieslbl.configure(fg="#16C1D4")
    imagelbl.configure(image=dice)
    guessentry.delete(0, END)


def hint(*args):
    global show
    global triedlbl
    if show == True:
        triedlbl.grid_forget()
        show = False
    else:
        triedlbl = Label(win, text=tried, bg="white", fg="black", borderwidth=5, relief="groove")
        triedlbl.grid(row=2, column=1, rowspan=2)
        print("forget")
        show = True

def defexit():
    exit()

difval = IntVar()
difval.set(2)

win.configure(bg="#261E36")

game = Label(win, text="Guess The Number", font=("Tahoma", 20), bg="#261E36", fg="#16C1D4", borderwidth=10, relief="groove")
game.grid(row=0, column=0, columnspan=3)

difficulty1 = Radiobutton(win, text="Easy(0-50)", value=1, variable=difval, bg="#261E36", fg="#16C1D4", borderwidth=5, relief="groove")
difficulty2 = Radiobutton(win, text="Normal(0-100)", value=2, variable=difval, bg="#261E36", fg="#16C1D4", borderwidth=5, relief="groove")
difficulty3 = Radiobutton(win, text="Impossible(0-200)", value=3, variable=difval, bg="#261E36", fg="#16C1D4", borderwidth=5, relief="groove")

difficulty1.grid(row=1, column=0, pady=10)
difficulty2.grid(row=1, column=1, pady=10)
difficulty3.grid(row=1, column=2, padx=8, pady=10)

explainlbl = Label(win, text="In this game you will try to find a secret number \nthat is randomly generated every round. \nTry to guess it with the least possible tries!", font=("Tahoma", 12), bg="#261E36", fg="#16C1D4")
explainlbl.grid(row=2, column=0, columnspan=3)

imagelbl = Label(win, image=dice, bg="#261E36")
imagelbl.grid(row=3, column=0, rowspan=2)

guessentry = Entry(win, width=10, state="disabled")
guessentry.grid(row=3, column=1)

trieslbl = Label(win, text="0", padx=20, borderwidth=7, relief="groove", bg="#261E36", fg="#16C1D4")
trieslbl.grid(row=4, column=1)

exitbtn = Button(win, text="Exit", height=3, width=14, bg="#16C1D4", command=defexit)
exitbtn.grid(row=3, column=2)

randomizebtn = Button(win, text="Randomize", height=3, width=14, bg="#16C1D4", command=rannum)
randomizebtn.grid(row=4, column=2)

status = Label(win, text="", bg="#261E36", fg="red")
status.grid(row=5, column=0, columnspan=3)

win.bind('<Return>', entercommand)
win.bind('<Control_L>', hint)

win.mainloop()
