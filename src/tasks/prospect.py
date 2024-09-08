import turtle

wn = turtle.Screen()
wn.title("Screen for painting")
wn.bgcolor("green")
wn.setup(width=600.0, height=600.0)

my_turtle = turtle.Turtle()


my_turtle.down()

my_turtle.left(45)
my_turtle.forward(100)
my_turtle.backward(100)
my_turtle.right(45)

my_turtle.forward(100)

my_turtle.left(45)
my_turtle.forward(100)
my_turtle.backward(100)
my_turtle.right(45)

my_turtle.right(90)
my_turtle.forward(100)

my_turtle.left(90)
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.backward(100)
my_turtle.right(45)
my_turtle.right(90)

my_turtle.right(90)
my_turtle.forward(100)

my_turtle.left(180)
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.backward(100)
my_turtle.right(45)
my_turtle.right(180)

my_turtle.right(90)

my_turtle.forward(100)
my_turtle.right(90)

my_turtle.left(45)
my_turtle.forward(100)

wn.mainloop()

