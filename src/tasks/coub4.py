import scrambambas

t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Screen for painting")
wn.bgcolor("green")
wn.setup(width=600.0, height=600.0)

wn.mainloop()
stepLength = 100
turnAngel = 90

t.goto(200, 200)
t.down()

t.right(45)
t.forward(100)
t.backward(100)
t.forward(100)
t.left(45)
t.forward(stepLength)

t.right(turnAngel)
t.right(45)
t.forward(100)
t.backward(100)
t.forward(100)
t.left(45)
t.forward(stepLength)

t.right(turnAngel)
t.right(45)
t.forward(100)
t.backward(100)
t.forward(100)
t.left(45)
t.forward(stepLength)

t.right(turnAngel)
t.right(45)
t.forward(100)
t.backward(100)
t.forward(100)
t.left(45)
t.forward(stepLength)

t.right(turnAngel)
t.right(45)

t.forward(stepLength)
t.right(turnAngel)

t.forward(stepLength)
t.right(turnAngel)

t.forward(stepLength)
t.right(turnAngel)

t.forward(stepLength)
t.right(turnAngel)
