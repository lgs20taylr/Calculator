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
  expression = expression.replace("pi",str(math.pi))
  expression = expression.replace("e",str(math.e))
  while "sin(" in expression:
      sin = re.search("sin((.*))", expression)
      sinner = str(sin[1])
      sinner = sinner.lstrip("sin(")
      sinner = sinner.partition(")")[0]
      dEyes = math.sin(float(sinner))
      if dEyes.is_integer():
        dEyes = int(dEyes)
      expression = expression.replace("sin("+sinner+")",str(dEyes))
  while "tan(" in expression:
    tan = re.search("tan((.*))", expression)
    tanner = str(tan[1])
    tanner = tanner.lstrip("sin(")
    tanner = tanner.partition(")")[0]
    smAnt = math.tan(float(tanner))
    if smAnt.is_integer():
      smAnt = int(smAnt)
    expression = expression.replace("tan("+tanner+")",str(smAnt))
  while "cos(" in expression:
    cos = re.search("cos((.*))", expression)
    cosSack = str(cos[1])
    cosSack = cosSack.lstrip("sin(")
    cosSack = cosSack.partition(")")[0]
    cuz = math.cos(float(cosSack))
    if cuz.is_integer():
      cuz = int(cuz)
    expression = expression.replace("cos("+cosSack+")",str(cuz))
  return eval(expression)
  
if __name__ == "__main__":
    main()