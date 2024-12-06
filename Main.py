#setup
import turtle
todd = turtle.Turtle()
todd.speed(0)
screen = turtle.Screen()
screen.setup(500, 500)

#functions
def square(t):
    t.pendown()
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.penup()
def triangle(t):
    t.pendown()
    for i in range(3):
        t.forward(50)
        t.left(120)
    t.penup()
def rectangle(t):
    t.pendown()
    for i in range(2):
        t.forward(75)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.penup()
def circle(t):
    t.pendown()
    t.circle(25)
    t.penup()
def hexagon(t):
    t.pendown()
    for i in range(6):
        t.forward(30)
        t.left(60)
    t.penup()


def MainLoop():
    #--------------- Slide 1 v
    todd.clear()
    todd.clearstamps()
    todd.shape("classic")
    screen.bgcolor("white")

    todd.penup()
    todd.goto(0,200)

    todd.write("All About Me", align="center", font=("Roboto", 24, "bold"))

    todd.goto(0,150)
    todd.write("by: Annjal Parajuli (enter to next slide)", align = "center", font = ("Calibri", 15, "italic"))

    todd.goto(-25,0)
    todd.fillcolor("skyblue")
    todd.begin_fill()
    square(todd)
    todd.end_fill()

    todd.goto(-150,-100)
    turtle.addshape("IRLTurtle.gif")
    todd.shape("IRLTurtle.gif")
    a = todd.stamp()

    todd.goto(150,-100)
    turtle.addshape("Computer.gif")
    todd.shape("Computer.gif")
    enter = input("Go to Next Slide?")

    #------------------------- Slide 2 v
    todd.clear()
    todd.clearstamps()
    todd.shape("classic")
    screen.bgcolor("skyblue")

    todd.penup()
    todd.goto(0,200)

    todd.write("Favorite Foods", align="center", font=("Roboto", 14, "bold"))

    todd.goto(0,150)
    todd.write("My favorite foods are dumplings, samosa, and chow mein. (enter to next slide)", align = "center", font = ("Calibri", 10, "italic"))

    todd.goto(-25,0)
    todd.fillcolor("green")
    todd.begin_fill()
    triangle(todd)
    todd.end_fill()

    todd.goto(-150,-100)
    turtle.addshape("Samosa.gif")
    todd.shape("Samosa.gif")
    a = todd.stamp()

    todd.goto(150,-100)
    turtle.addshape("Dumpling.gif")
    todd.shape("Dumpling.gif")
    enter = input("Go to Next Slide?")

    #------------------------------- Slide 3 v
    todd.clear()
    todd.clearstamps()
    todd.shape("classic")
    screen.bgcolor("green")

    todd.penup()
    todd.goto(0,200)

    todd.write("Hobbies", align="center", font=("Roboto", 24, "bold"))

    todd.goto(0,150)
    todd.write("My hobbies are rubix cubes, badminton, coding, and video games. (enter to next slide)", align = "center", font = ("Calibri", 10, "italic"))

    todd.goto(-37.5,0)
    todd.fillcolor("purple")
    todd.begin_fill()
    rectangle(todd)
    todd.end_fill()

    todd.goto(-150,-100)
    turtle.addshape("Rubix.gif")
    todd.shape("Rubix.gif")
    a = todd.stamp()

    todd.goto(150,-100)
    turtle.addshape("Badminton.gif")
    todd.shape("Badminton.gif")
    enter = input("Go to Next Slide?")

    #------------------------- Slide 4 v
    todd.clear()
    todd.clearstamps()
    todd.shape("classic")
    screen.bgcolor("purple")

    todd.penup()
    todd.goto(0,200)

    todd.write("Favorite Movie", align="center", font=("Roboto", 24, "bold"))

    todd.goto(0,150)
    todd.write("My favorite movie is The Wild Robot. (enter to next slide)", align = "center", font = ("Calibri", 15, "italic"))

    todd.goto(-0,0)
    todd.fillcolor("red")
    todd.begin_fill()
    circle(todd)
    todd.end_fill()

    todd.goto(-150,-100)
    turtle.addshape("Robot.gif")
    todd.shape("Robot.gif")
    a = todd.stamp()

    todd.goto(150,-100)
    turtle.addshape("WildRobot.gif")
    todd.shape("WildRobot.gif")
    enter = input("Go to Next Slide?")

    #---------------------- slide 5 v
    todd.clear()
    todd.clearstamps()
    todd.shape("classic")
    screen.bgcolor("red")

    todd.penup()
    todd.goto(0,200)

    todd.write("Favorite Sport", align="center", font=("Roboto", 24, "bold"))

    todd.goto(0,150)
    todd.write("My favorite sport is soccer. (enter to next slide)", align = "center", font = ("Calibri", 15, "italic"))

    todd.goto(-15,0)
    todd.fillcolor("white")
    todd.begin_fill()
    hexagon(todd)
    todd.end_fill()

    todd.goto(-150,-100)
    turtle.addshape("Soccer.gif")
    todd.shape("Soccer.gif")
    a = todd.stamp()

    todd.goto(150,-100)
    turtle.addshape("Messi.gif")
    todd.shape("Messi.gif")

running = True
while running:
    MainLoop()
    question = input("Do you want to see it again? (Press y/n)")
    if question != "y":
        running = False

