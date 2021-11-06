import turtle

from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

#gui stuff
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid() #set tk to grid
ttk.Label(frm, text="Colour picker").grid(column=0, row=0)

#colour picker
rS = Scale(root, from_=0, to=255, bg="#FF0000")
rS.grid(column=1, row=0)
rS.set(255)


gS = Scale(root, from_=0, to=255, bg="#00FF00")
gS.grid(column=2, row=0)


bS = Scale(root, from_=0, to=255, bg="#0000FF")
bS.grid(column=3, row=0)

sizeS = Scale(root, from_=0, to=50)
sizeS.grid(column=5, row=0)


#movement

def forward():
  if (t.pos()[0]+10 <= screen.screensize()[0]/2) or (t.pos()[0]-10 >= -screen.screensize()[0]/2):
    t.fd(10)

def back():
  t.bk(10)

def left():
  t.lt(5)
  
def right():
  t.rt(5)

#pen
def pUp():
  t.penup()
  
def pDown():
  t.pendown()

#colour
def red():
  t.color("#FF0000")

def green():
  t.color("#00FF00")

def blue():
  t.color("#0000FF")

turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.shape("turtle")
t.color("orange")
t.pu()
#screen.screensize(500, 500)


while True:
  screen.listen()
  screen.update()
  t.color((rS.get(), gS.get(), bS.get()))
  t.pensize(sizeS.get())






  #movement
  screen.onkey(forward , "w")
  screen.onkey(back , "s")
  screen.onkey(left , "a")
  screen.onkey(right , "d")

  #pen
  screen.onkey(pUp , "Up")
  screen.onkey(pDown , "Down")

  print("TurtlePos:", t.pos(), "ScreenSize:", screen.screensize())
  

  
  
  
  
  
  
  
  
  