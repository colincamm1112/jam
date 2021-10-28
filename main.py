# Cookie Clicker
# Simple Cookie Clicker Clone
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech
import turtle



wn = turtle.Screen()

wn.bgcolor("black")
wn.register_shape("cookie.gif")


button1 = turtle.Turtle()

button1.penup()
button1.shape("square")
button1.color("blue")
button1.goto(-200,100)

button1.penup()







cookie = turtle.Turtle()

cookie.shape("circle")
cookie.color("red")
cookie.size = 30
cookie.speed(0)



clicks = float(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 300)
pen.write(clicks, font=("Courier New", 32, "normal"))


def glo():
  if clicked1 and clicks >= 15:
    clicks -= 15




def clicked1(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(clicks, font=("Courier New", 32, "normal"))

def clicked2(x, y):
  
  global clicks
  if clicks >=15:
    if glo:
      clicks -= 15
      while True: 
        clicks += (.0000001)
       


cookie.onclick(clicked1)
button1.onclick(clicked2)


wn.mainloop()