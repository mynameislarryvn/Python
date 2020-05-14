import turtle
import time
import random

screen = turtle.Screen()
screen.title("BRUHHHHHHHHHHHHHHHHHH")
screen.bgcolor("black")
screen.setup(width=400, height=600)
screen.tracer(0)
pixel = 40
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

bodyparts = []

delay = 1
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + pixel)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - pixel)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + pixel)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - pixel)

screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")

while True:
    screen.update()

    if head.distance(food) < pixel:
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        food.goto(x,y)

        new_bodypart = turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("square")
        new_bodypart.color("grey")
        new_bodypart.penup()
        bodyparts.append(new_bodypart)

    for index in range(len(bodyparts)-1, 0 , -1):
        x = bodyparts[index - 1].xcor()
        y = bodyparts[index - 1].ycor()
        bodyparts[index].goto(x, y)

    if len(bodyparts) > 0:
        x = head.xcor()
        y = head.ycor()
        bodyparts[0].goto(x, y)


    move()

    time.sleep(delay)

screen.mainloop()



