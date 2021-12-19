from turtle import *
from time import sleep

t = Turtle()
t.up()
t.shape("circle")
initialYPos = 200
initialXPos = -400
t.goto(initialXPos, initialYPos)
# t.down()
t.speed("fastest")

line = Turtle()
line.up()
line.goto(-600,0)
line.down()
line.goto(600,0)

g = 9.8

horizontalVelocity = 10
verticalVelocity = 0

def getXpos(V,t):
    return V * t

def getYpos(t):
    return 0.5 * g * t**2

def getYvel(t):
    return g * t

def fall(initialXPos, initialYPos):
    time = 0
    c = 0
    while t.ycor() - 12 >= 0:
        t.goto(initialXPos+getXpos(horizontalVelocity,time), initialYPos-getYpos(time))

        # if c%40 == 0: t.write(t.ycor(),align="left")
        # if c%40 == 0: t.write(time,align="right")

        time += 0.05
        c += 1
    t.impactVelocity = getYvel(time)
    print(time)
    t.impactX = t.xcor()


corBall = 0.75

def getBounceYVel(vi, t):
    return vi - g * t

def bounceY(v,t):
    return v*t + 0.5 * (-g) * t**2

def bounce():
    time = 0
    c = 0
    initialYVel = t.impactVelocity * corBall

    while getBounceYVel(initialYVel,time) >= 0:
        t.goto(t.impactX + getXpos(horizontalVelocity,time), bounceY(initialYVel,time)+12)
        
        # if c%40 == 0: t.write(t.ycor())
        # if c%40 == 0: print(getBounceYVel(initialYVel,time))


        time += 0.05
        c += 1
    return t.xcor(), t.ycor();
    
    
fall(initialXPos, initialYPos)
while True:
    if t.ycor() - 12 <= 0:
        xPos, yPos = bounce()
        fall(xPos,yPos)

print(abs(initialXPos) - abs(t.xcor()))


exitonclick()