import turtle
turtle.tracer(3)
screen = turtle.Screen() 
screen.bgpic("background.gif")  
screen.setup(800,539)   


turtle.addshape("Sun.gif")  
sun = turtle.Turtle()
sun.shape("Sun.gif")

turtle.addshape("Earth.gif")
earth = turtle.Turtle()
earth.shape("Earth.gif")

turtle.addshape("Mercury.gif")
mercury = turtle.Turtle()
mercury.shape("Mercury.gif")


mercury.penup()
mercury.goto(0,-90)

earth.penup()
earth.goto(0,-200)

while True:
    mercury.circle(90,360/88) 
    earth.circle(200,360/365)
    turtle.update() 
  
