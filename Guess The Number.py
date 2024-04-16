import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk

def clear():
    global result
    result = ""
    var.set(result)

def equal():
    try:
        global result
        calculate = eval(result)
        var.set(calculate)
        result = str(calculate)
    except:
        result = "error"
        var.set(result)

def press(number):
    global result
    if result == "error":
        result = ""
    result += str(number)
    var.set(result)

win = ThemedTk(theme="breeze")
win.configure(themebg="breeze")

result = ""
var = tkinter.StringVar()

win.title("")
win.geometry("185x190")
win.resizable(False, False)
win.iconbitmap("calculator.ico")

but1 = ttk.Button(text="1", width=3, command = lambda: press(1))
but2 = ttk.Button(text="2", width=3, command = lambda: press(2))
but3 = ttk.Button(text="3", width=3, command = lambda: press(3))
but4 = ttk.Button(text="4", width=3, command = lambda: press(4))
but5 = ttk.Button(text="5", width=3, command = lambda: press(5))
but6 = ttk.Button(text="6", width=3, command = lambda: press(6))
but7 = ttk.Button(text="7", width=3, command = lambda: press(7))
but8 = ttk.Button(text="8", width=3, command = lambda: press(8))
but9 = ttk.Button(text="9", width=3, command = lambda: press(9))
but0 = ttk.Button(text="0", width=3, command = lambda: press(0))

butclear = ttk.Button(text="C", width=3, command=clear)
butcomma = ttk.Button(text=".", width=3, command = lambda: press("."))
butplus = ttk.Button(text="+", width=3, command = lambda: press("+"))
butminus = ttk.Button(text="-", width=3, command = lambda: press("-"))
butmul = ttk.Button(text="x", width=3, command = lambda: press("*"))
butdiv = ttk.Button(text="/", width=3, command = lambda: press("/"))
butpower = ttk.Button(text="^", width=3, command = lambda: press("**"))
buteq = ttk.Button(text="=", width=3, command = equal)
butparleft = ttk.Button(text="(", width=3, command = lambda: press("("))
butparright = ttk.Button(text=")", width=3, command = lambda: press(")"))
showentry = ttk.Entry(win, width=24, textvariable=var, state="readonly")

showentry.grid(row=0, column=0, columnspan=6)
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)
but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
but7.grid(row=3, column=0)
but8.grid(row=3, column=1)
but9.grid(row=3, column=2)
but0.grid(row=4, column=1)
butcomma.grid(row=4, column=0)
butclear.grid(row=4, column=2)
butplus.grid(row=1, column=3)
butminus.grid(row=2, column=3)
butmul.grid(row=3, column=3)
butdiv.grid(row=4, column=3)
butparleft.grid(row=5, column=0)
butparright.grid(row=5, column=1)
butpower.grid(row=5, column=2)
buteq.grid(row=5, column=3)

win.mainloop()
