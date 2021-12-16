from turtle import *
from time import sleep

t = Turtle()
t.shape("circle")
t.up()
t.initialPos = 450
t.goto(0, t.initialPos)
#t.down()
t.speed("fastest")

line = Turtle()
line.up()
line.goto(-200,0)
line.down()
line.goto(200, 0)

g = 9.8

def getVelocity(t):
    return g * t

def getYpos(t):
    return 0.5 * g * t**2

def fall(initialPos):
    time = 0
    c = 0
    while t.ycor() -12 >= line.ycor():
        t.goto(0, initialPos - getYpos(time))
        
        #if c%40 == 0: t.write(t.ycor(), align="left")
        if c%40 == 0: print(getVelocity(time))

        c += 1
        time += 0.025
    t.impactVelocity = getVelocity(time)
    print(t.impactVelocity)

corBall = 0.75

def getBounceVel(vi, t):
    return vi - g * t

def bounceY(v,t):
    return v*t + 0.5 * (-g) * t**2

def bounce():
    time = 0
    c = 0
    bounceHeight = t.initialPos * corBall**2
    initialVelocity = t.impactVelocity * corBall
    initialPos = 0

    while getBounceVel(initialVelocity,time) >= 0:
        t.goto(0, bounceY(initialVelocity,time)+12)
        
        #if c%40 == 0: t.write(t.ycor())
        if c%40 == 0: print(getBounceVel(initialVelocity,time))


        time += 0.025
        c += 1
    return t.ycor()
        
fall(t.initialPos)
while True:
    if t.ycor() - 12 <= 0:
        fall(bounce())

exitonclick()