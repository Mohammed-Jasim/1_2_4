import turtle as trtl
import random as rand

#Creation of the maze turtle
maze = trtl.Turtle()
maze.pensize(3)
maze.hideturtle()
maze.speed(0)

#Adding wn and changing the background color
wn = trtl.Screen()
wn.bgcolor("#EEE1B3")

#Creation of the title turtle
writer = trtl.Turtle()
writer.hideturtle()
writer.penup()

#Creation of timer 
time_writer = trtl.Turtle()
time_writer.penup()
time_writer.hideturtle()

#Creation of the maze runner
mr = trtl.Turtle()
colorlist = ['red', 'blue', 'green', 'orange', 'black', 'yellow', 'purple', 'brown', 'gray']
mr.color(colorlist[rand.randint(1,9)])
shapelist = ['circle', 'square', 'arrow', 'triangle', 'turtle']
mr.shape(shapelist[rand.randint(1,5)])
mr.penup()
mr.hideturtle()
mr.goto(-55, 20)
mr.pendown()
mr.showturtle()

#Creation of buttons for the speed of maze runner
button1 = trtl.Turtle()
button2 = trtl.Turtle()
button3 = trtl.Turtle()
button4 = trtl.Turtle()
wn.addshape("button1.gif")
wn.addshape("button2.gif")
wn.addshape("button3.gif")
wn.addshape("button4.gif")
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

### CREATION OF MAZE
#Function to make the first 4 walls not drawn

def pen():
    if walls > walls4:  
        maze.penup()
    else:
        maze.pendown()
#Function to draw the door
def door(am):
    maze.fd(am-doorcor)
    maze.penup()
    maze.fd(10)
    pen()
#Function to draw the barrier
def barrier(am):
    maze.forward(am-barriercor)
    maze.left(90)
    maze.forward(path_width)
    maze.back(path_width)
    maze.right(90)
fd = 84
bd = 42
path_width = 30
diffuculty = input("How difficult would you like the maze to be?(easy, medium, hard, extreme): ")
if diffuculty == "easy":
    walls = 15
    writer.goto(-190, 250)
    writer.write("Maze Runner", font=("Arial", 34, "bold")) 
elif diffuculty == "medium":
    walls = 25
    writer.goto(-190, 320)
    writer.write("Maze Runner", font=("Arial", 34, "bold")) 
elif diffuculty == "hard":
    writer.goto(-190, 380)
    writer.write("Maze Runner", font=("Arial", 34, "bold")) 
    walls = 35
elif diffuculty == "extreme":
    walls = 48
    writer.goto(-190, 480)
    writer.write("Maze Runner", font=("Arial", 34, "bold")) 
walls4 = walls - 4
#Creation of the actual maze
for i in range(walls):
    pen()
    doorcor = rand.randint(20, fd - bd)
    barriercor = rand.randint(20, fd- bd)
    maze.lt(90)
    maze.fd(30)
    if doorcor > barriercor:
        barrier(doorcor)
        door(doorcor*2)
        sum1 = doorcor*2 - barriercor
        maze.fd(fd - sum1)
        fd += 15
        bd += 8
        walls -= 1
    else:
        door(barriercor)
        barrier(barriercor*2)
        sum2 = barriercor*2 - doorcor
        maze.fd(fd - sum2)
        fd += 16
        bd += 8
        walls -= 1

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
countdown()



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
