import turtle
colors=["red","yellow","blue","green","black"]
turtle1 = turtle.Turtle()
turtle1.speed(221)
 
for x in range(211): 
    turtle.pencolor(colors[x%5])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)


   