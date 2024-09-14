import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.color("blue", "Yellow")
my_turtle.shape("Triangle")
my_turtle.pensize(5)
my_turtle.speed(3)
my_turtle.begin_fill()

my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)

my_turtle.end_fill()

my_turtle.color("red", "green")
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed(8)
my_turtle.begin_fill()

my_turtle.penup()
my_turtle.goto(x=8, y=100)
my_turtle.pendown()

my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

my_turtle.color("red", "purple")
my_turtle.shape("arrow")
my_turtle.pensize(2)
my_turtle.speed(5)










