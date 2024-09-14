import turtle

window = turtle.Screen()
window.title("Повноекранне вікно для черепашки")           # Вказуємо назву вікна для малювання
window.setup(width=700, height=700)                        # Вказуємо розмірність нашого вікна (int числа більше 1 = розмір у пікселях, float числа >= 1 розмір вікна у %)

my_turtle = turtle.Turtle()

my_turtle.forward(100)
my_turtle.up()
my_turtle.forward(50)
my_turtle.down()
my_turtle.forward(100)

my_turtle.up()
my_turtle.goto(x=100, y=100)
my_turtle.down()
my_turtle.forward(50)

my_turtle.reset()

my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)

my_turtle.reset()

my_turtle.forward(180)
my_turtle.left(72)
my_turtle.forward(180)
my_turtle.left(72)
my_turtle.forward(180)
my_turtle.left(72)
my_turtle.forward(180)
my_turtle.left(72)
my_turtle.forward(180)

my_turtle.reset()

my_turtle.forward(180)
my_turtle.left(60)
my_turtle.forward(180)
my_turtle.left(60)
my_turtle.forward(180)
my_turtle.left(60)
my_turtle.forward(180)
my_turtle.left(60)
my_turtle.forward(180)
my_turtle.left(60)
my_turtle.forward(180)
my_turtle.left(60)

turtle.done()
window.mainloop()