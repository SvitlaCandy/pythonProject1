import turtle

user_input = input("Склільки кутів має бути у фігури_\n")
user_color = input("Якого кольору має бути фігура?\n")

screen = turtle.Screen()

my_turtle = turtle.Turtle()

if user_color == "Red" or user_color == "red":
    my_turtle.pencolor("Red")

elif user_color == "Blue" or user_color == "blue":
    my_turtle.pencolor("Blue")

elif user_color == "Green" or user_color == "green":
    my_turtle.pencolor("Green")

elif user_color == "Yellow" or user_color == "yellow":
    my_turtle.pencolor("Yellow")

if user_input == "3":

    my_turtle.forward(90)
    my_turtle.right(120)
    my_turtle.forward(90)
    my_turtle.right(120)
    my_turtle.forward(90)
    my_turtle.right(120)

elif user_input == "4":

    my_turtle.forward(90)
    my_turtle.right(90)
    my_turtle.forward(90)
    my_turtle.right(90)
    my_turtle.forward(90)
    my_turtle.right(90)
    my_turtle.forward(90)
    my_turtle.right(90)

elif user_input == "5":

    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)

screen.mainloop()