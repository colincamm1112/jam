
import turtle


wn = turtle.Screen()
wn.bgcolor("black")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = -1
grav = 0.1
clicks  = 0
ball.dx = 4




pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,200)
pen.write(clicks, font=("Courier New", 32, "normal"))

def point():
  global clicks 
  clicks += 1
  pen.clear()
  pen.write(clicks, font=("Courier New", 32, "normal"))



while True:
  wn.update()
  ball.dy -= grav
  ball.sety(ball.ycor() + ball.dy)
  
  ball.setx(ball.xcor() + ball.dx)

  if ball.ycor() < -220:
    ball.dy *= -1
    point()
  
  if ball.xcor() < -300:
    ball.dx *= -1
    point()
  
  if ball.xcor() > 300:
    ball.dx *= -1
    point()



wn.mainloop()