import turtle
colors=["red","blue","green","black"]
my_turtle = turtle.Turtle() 

my_turtle.speed(20)
for i in range(123):  
    
    my_turtle.pencolor(colors[i%4])
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(17)



input()