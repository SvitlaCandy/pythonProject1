import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Screen for painting")
wn.bgcolor("green")
wn.setup(width=600.0, height=600.0)

wn.mainloop()

t.goto(100, 100)
t.down()
t.forward(100)
t.up()

t.goto(200, 100)
t.down()
t.forward(100)
t.up()


