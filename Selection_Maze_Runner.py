import turtle as trtl
import random as rand

#Creation of the maze turtle
maze2 = trtl.Turtle()
maze2.pensize(3)
maze2.hideturtle()
maze2.speed(0)

#Adding wn and changing the background color
wn = trtl.Screen()
wn.bgcolor("#EEE1B3")

#Creation of the title turtle
writer = trtl.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-300, 250)
writer.write("How difficult would you like the maze to be?:", font=("Arial", 22, "bold")) 
#Creation of timer
time_writer = trtl.Turtle()
time_writer.penup()
time_writer.hideturtle()

#Creation of the maze runner
mr = trtl.Turtle()
mr.hideturtle()
colorlist = ['red', 'blue', 'green', 'orange', 'black', 'yellow', 'purple', 'brown', 'gray']
mr.color(colorlist[rand.randint(0,8)])
shapelist = ['circle', 'square', 'arrow', 'triangle', 'turtle']
mr.shape(shapelist[rand.randint(0,4)])
mr.penup()
mr.hideturtle()
mr.goto(-55, 20)
mr.pendown()
mr.shapesize(1)

#Creation of the diffuculty selection buttons
diffbutton1 = trtl.Turtle()
diffbutton2 = trtl.Turtle()
diffbutton3 = trtl.Turtle()
diffbutton4 = trtl.Turtle()
wn.addshape("Easy.gif")
wn.addshape("Medium.gif")
wn.addshape("Hard.gif")
wn.addshape("Extreme.gif")

diffbutton1.penup()
diffbutton2.penup()
diffbutton3.penup()
diffbutton4.penup()
diffbutton1.hideturtle()
diffbutton2.hideturtle()
diffbutton3.hideturtle()
diffbutton4.hideturtle()
diffbutton1.shape("Easy.gif")
diffbutton2.shape("Medium.gif")
diffbutton3.shape("Hard.gif")
diffbutton4.shape("Extreme.gif")
diffbutton1.goto(-300, 0)
diffbutton2.goto(-100, 0)
diffbutton3.goto(100, 0)
diffbutton4.goto(300, 0)
diffbutton1.showturtle()
diffbutton2.showturtle()
diffbutton3.showturtle()
diffbutton4.showturtle()
def easy(x,y):
    maze(15)
    writer.goto(-190, 250)
    writer.write("Maze Runner", font=("Arial", 34, "bold"))
    countdown()
def medium(x,y): 
    maze(25)
    writer.goto(-190, 320)
    writer.write("Maze Runner", font=("Arial", 34, "bold"))
    countdown()
def hard(x,y):
    maze(35)
    writer.goto(-190, 380)
    writer.write("Maze Runner", font=("Arial", 34, "bold"))
    countdown()
def extreme(x,y):
    maze(48)
    writer.goto(-190, 480)
    writer.write("Maze Runner", font=("Arial", 34, "bold"))
    countdown()

diffbutton1.onclick(easy)
diffbutton2.onclick(medium)
diffbutton3.onclick(hard)
diffbutton4.onclick(extreme)
#Creation of buttons for the speed of maze runner
button1 = trtl.Turtle()
button2 = trtl.Turtle()
button3 = trtl.Turtle()
button4 = trtl.Turtle()
wn.addshape("button1.gif")
wn.addshape("button2.gif")
wn.addshape("button3.gif")
wn.addshape("button4.gif")
button1.hideturtle()
button2.hideturtle()
button3.hideturtle()
button4.hideturtle()
button1.shape("button1.gif")
button2.shape("button2.gif")
button3.shape("button3.gif")
button4.shape("button4.gif")
button1.penup()
button1.speed(0)
button1.goto(-600, 200)
button2.penup()
button2.speed(0)
button2.goto(-600, 50)
button3.penup()
button3.speed(0)
button3.goto(-600, -100)
button4.penup()
button4.speed(0)
button4.goto(-600, -250)
button1.showturtle()
button2.showturtle()
button3.showturtle()
button4.showturtle()

### CREATION OF MAZE
#Function to make the first 4 walls not drawn


#Function to draw the door


def maze(wall):
    writer.clear()
    mr.showturtle()
    diffbutton1.hideturtle()
    diffbutton2.hideturtle()
    diffbutton3.hideturtle()
    diffbutton4.hideturtle()
    fd = 84
    bd = 42
    path_width = 30
    walls4 = wall - 4
    def pen():
        if wall > walls4:  
            maze2.penup()
        else:
            maze2.pendown()
    #Function to draw the door
    def door(am):
        maze2.fd(am-doorcor)
        maze2.penup()
        maze2.fd(10)
        pen()
    #Function to draw the barrier
    def barrier(am):
        maze2.forward(am-barriercor)
        maze2.left(90)
        maze2.forward(path_width)
        maze2.back(path_width)
        maze2.right(90)
    #Creation of the actual maze
    for i in range(wall):
        pen()
        doorcor = rand.randint(20, fd - bd)
        barriercor = rand.randint(20, fd- bd)
        maze2.lt(90)
        maze2.fd(30)
        if doorcor > barriercor:
            barrier(doorcor)
            door(doorcor*2)
            sum1 = doorcor*2 - barriercor
            maze2.fd(fd - sum1)
            fd += 15
            bd += 8
            wall -= 1
        else:
            door(barriercor)
            barrier(barriercor*2)
            sum2 = barriercor*2 - doorcor
            maze2.fd(fd - sum2)
            fd += 16
            bd += 8
            wall -= 1

#Timer
timer = 0
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#Timer shown on screen function
def countdown():
    global timer, timer_up
    writer.goto(-680, 300)
    time_writer.goto(-560, 300)
    timer += 1
    writer.write("Timer:", font=("Arial", 25, "bold"))
    time_writer.clear()
    time_writer.write(timer, font=("Arial", 25, "bold"))
    time_writer.getscreen().ontimer(countdown, counter_interval)


def move_runner():
    mr.forward(10)
def right():
    mr.setheading(0)
    move_runner()
def up():
    mr.setheading(90)
    move_runner()
def left():
    mr.setheading(180)
    move_runner()
def down():
    mr.setheading(270)
    move_runner()
wn.onkeypress(right, "d")
wn.onkeypress(up, "w")
wn.onkeypress(left, "a")
wn.onkeypress(down, "s")
def button1function(x,y):
    mr.speed(2.5)
def button2function(x,y):
    mr.speed(5)
def button3function(x,y):
    mr.speed(7.5)
def button4function(x,y):
    mr.speed(0)
button1.onclick(button1function)
button2.onclick(button2function)
button3.onclick(button3function)
button4.onclick(button4function)

wn.listen() 
wn.mainloop()
