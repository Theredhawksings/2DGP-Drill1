import turtle as t

t.shape("turtle")
t.colormode(255)
t.pencolor(96, 255, 209)
t.pensize(5)

def move_up():
    t.setheading(90)
    t.forward(50)
    t.stamp()

def move_left():
    t.setheading(180)
    t.forward(50)
    t.stamp()

def move_down():
    t.setheading(270)
    t.forward(50)
    t.stamp()

def move_right():
    t.setheading(360)
    t.forward(50)
    t.stamp()

def move_reset():
    t.reset()
    t.shape("turtle")
    t.colormode(255)
    t.pencolor(96, 255, 209)
    t.pensize(5)


t.onkey(move_up, 'w')
t.listen()

t.onkey(move_left, 'a')
t.listen()

t.onkey(move_down, 's')
t.listen()

t.onkey(move_right, 'd')
t.listen()

t.onkey(move_reset, 'Escape')
t.listen()


t.done()
