import math
import re
from tkinter import *

def main():
    window = Tk()
    window.geometry("400x100")
    window.title("Calculator")

    display = Label(window, text="")
    display.grid(column=6,row=0,columnspan=4)

    equationBox = Text(window,height=2,width=20)
    equationBox.grid(column=0,row=0,columnspan=4)

    equals = Button(window,text="=",command=lambda: pushToDisplay(calc(equationBox.get(1.0,END)),display), width=5)
    equals.grid(column=5, row=0, columnspan=1)

    window.mainloop()

def pushToDisplay(displayMe,display):
    display.config(text=displayMe)

def calc(expression):
    
    return eval(expression)

if __name__ == "__main__":
    main()
