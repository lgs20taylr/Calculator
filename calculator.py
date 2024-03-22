import math
import re
from tkinter import *

def main():
   window = Tk()
   window.geometry("400x100")
   window.title("Calculator")

   display = Label(window, text="", font=("Lucida Sans Typewriter", 10))
   display.grid(column=6,row=0,columnspan=4)

   equationBox = Text(window,height=2,width=20)
   equationBox.grid(column=0,row=0,columnspan=4)

   equals = Button(window,text="=",command=lambda: pushToDisplay(calc(equationBox.get(1.0,END)),display), width=5)
   equals.grid(column=5, row=0, columnspan=1)

   window.mainloop()

def pushToDisplay(displayMe,display):
   display.config(text=displayMe)

def calc(expression):
  expression = str(expression)
  expression = expression.replace("pi",str(math.pi))
  expression = expression.replace("e",str(math.e))
  while "sin(" in expression:
     expression = trespass(expression)
  while "tan(" in expression:
     expression = bronzer(expression)
  while "cos(" in expression:
     expression = beCosISaidSo(expression)
  while "|" in expression:
     expression = absolutelyClass(expression)
  return eval(expression)

def getTheThingy(matchMe,l,r):
   thingy = str(matchMe[1])
   thingy = thingy.lstrip(l)
   thingy = thingy.partition(r)[0]
   return thingy

def trespass(expression):
   sin = re.search("sin((.*))", expression)
   sinner = getTheThingy(sin,"sin(",")")
   dEyes = math.sin(float(sinner))
   if dEyes.is_integer():
      cuz = int(cuz)
   expression = expression.replace("sin("+sinner+")",str(dEyes))
   return expression

def bronzer(expression):
   tan = re.search("tan((.*))", expression)
   tanner = getTheThingy(tan,"tan(",")")
   smAnt = math.tan(float(tanner))
   if smAnt.is_integer():
      smAnt = int(smAnt)
   expression = expression.replace("tan("+tanner+")",str(smAnt))
   return expression

def beCosISaidSo(expression):
   cos = re.search("cos((.*))", expression)
   cosSack = getTheThingy(cos,"cos(",")")
   cuz = math.cos(float(cosSack))
   if cuz.is_integer():
      cuz = int(cuz)
   expression = expression.replace("cos("+cosSack+")",str(cuz))
   return expression

def absolutelyClass(expression):
   abso = re.search("abs((.*))", expression)
   lets = getTheThingy(abso,"abs(",")")
   go = abs(float(lets))
   if go.is_integer():
      go = int(go)
   expression = expression.replace("sin("+go+")",str(lets))
   return expression

if __name__ == "__main__":
    main()