import turtle
import time
import random

# We set up turtles here.
turtle.mode("logo")

win=turtle.Screen()

border=turtle.Turtle()
border.speed(0)
border.ht()
border.pu()

stab=turtle.Turtle()
stab.ht()
stab.pu()
stab.speed(0)
stab.goto(400,350)
stab.setheading(0)

snum=turtle.Turtle()
snum.ht()
snum.pu()
snum.speed(0)
snum.goto(475,265)

blt=turtle.Turtle()    
blt.pu()
blt.shape("triangle")
blt.color("darkblue")
blt.setheading(0)
blt.speed(0)
blt.goto(0,-300)

zombie=turtle.Turtle()
zombie.speed(0)
zombie.ht()
zombie.pu()
zombie.goto(-300+2*100,350)

gover=turtle.Turtle()
gover.ht()
gover.pu()

message=turtle.Turtle()
message.ht()
message.pu()

# We create general variables here.
score=0
gamesit=1
seconds=time.time()
localtime=time.ctime(seconds)

# We define general functions here for be able to change them easily.

# General screen setup
def fwindow():
    win.title("zombie game")
    win.bgcolor("gray")
    win.setup(width=1200,height=800)
    win.listen()

# General game border setup
def drawborder():
    border.goto(-350,350)
    border.pensize(5)
    border.pencolor("black")
    border.pd()
    for i in range(4):
        border.rt(90)
        border.fd(700)
    border.pu()
    border.goto(-350,-250)
    border.rt(90)
    border.pd()
    border.fd(700)
    
# Scoreboard drawing function
def drawstab():
    stab.pensize(5)
    stab.pd()
    for i in range(2):
        stab.rt(90)
        stab.fd(150)
        stab.rt(90)
        stab.fd(90)
    stab.bk(50)
    stab.setheading(90)
    stab.fd(150)
    stab.pu()
    stab.goto(475,315)
    stab.write("YOUR SCORE",False,"center",("Arial",12,"bold"))
    snum.write(score,False,"center",("Arial",15,"bold"))

# Intoduction text
def mess():
    message.goto(-475,185)
    message.write("Try to shoot zombies\nbefore they arrive\nYOUR BASE!\n\n'A' for left\n'D' for right\n'W' for fire",False,"center",("Arial",12,"bold"))

# Gameover screen function
def gameover():
    gamesit=0
    stab.clear()
    snum.clear()
    blt.clear()
    zombie.clear()
    border.clear()
    message.clear()
    win.bgcolor("red")
    gover.pencolor("white")
    gover.write("    GAME OVER :(\nYOUR SCORE IS: "+str(score),True,"center",("Arial",25,"bold"))
    turtle.exitonclick()

# Score function
def scoreup():
    if(gamesit==1):
        global score
        score=score+1
        snum.clear()
        snum.write(score,False,"center",("Arial",15,"bold"))
        zombie.goto(-300+(random.choice([0,1,2,3,4,5,6]))*100,350)

# Player move functions 
def go_lt():
    if(gamesit==1,blt.ycor()==-250,blt.xcor()>-300):    
        blt.speed(11)
        blt.setheading(270)
        blt.fd(100)
        blt.setheading(0)
    
def go_rt():
    if(gamesit==1,blt.ycor()==-250,blt.xcor()<300):
        blt.speed(11)
        blt.setheading(90)
        blt.fd(100)
        blt.setheading(0)   

# Firing function
def fire():
    if(gamesit==1,blt.ycor()==-300):
        blt.speed(2)
        blt.fd(650)
        blt.ht()
        blt.speed(0)
        blt.bk(650)
        if(blt.xcor()==zombie.xcor()):
            scoreup()
        elif(blt.xcor()==0 and zombie.xcor()==0):
            scoreup()
        blt.st()
        
# Zombie move function
def zmove():
    gamesit=1
    while (gamesit==1):
        if(zombie.ycor()>-250):        
            time.sleep(0.1+(random.randrange(0,20,1))*0.01)
            zombie.fd(50)
        if(zombie.ycor()==-250):
            zombie.goto(-500,-500)
            blt.ht()
            blt.goto(500,500)
            gameover()
            

# Zombie respawn function
def spawn_zombie():
    if(gamesit==1):
        zombie.shape("square")
        zombie.shapesize(1.5)
        zombie.color("green")
        zombie.st()
        zombie.setheading(180)
        zmove()

# Mainloop
turtle.listen()
turtle.update()
turtle.onkey(fire,'w')
turtle.onkey(go_lt,'a')
turtle.onkey(go_rt,'d')
fwindow()
drawborder()
mess()
drawstab()
spawn_zombie()

turtle.mainloop()