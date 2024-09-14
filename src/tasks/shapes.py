import turtle

wn = turtle.Screen()
wn.title("Screen for painting")
wn.bgcolor("green")
wn.setup(width=600.0, height=600.0)

my_turtle = turtle.Turtle()


my_turtle.down()


my_turtle.left(90)
my_turtle.forward(200)

my_turtle.up()
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.down()

my_turtle.left(90)
my_turtle.forward(200)


wn.mainloop()

