import turtle
colors=["red","blue","green","black","brown"]
my_turtle = turtle.Turtle() 


my_turtle.speed(70)
for i in range(276):  
    
    my_turtle.pencolor(colors[i%5])
  
    my_turtle.left(70)     #(a)
    my_turtle.forward(100) #(a)
    my_turtle.left(55)     #(a)
    my_turtle.backward(100)  #(a)
    my_turtle.forward(50)   #(a)
    my_turtle.left(55)     #(a)
    my_turtle.forward(50)    #(a)
    my_turtle.backward(50)  #(a)
    my_turtle.left(124)  #(a)
    my_turtle.forward(50)   #(a)
      
    my_turtle.left(150)    
    my_turtle.forward(100) 
    my_turtle.right(150)  
    my_turtle.forward(60) 
    my_turtle.right(60)  
    my_turtle.backward(60) 
    my_turtle.left(30)  
    my_turtle.forward(100) 


    my_turtle.left(150)     #(a)
    my_turtle.forward(100) #(a)
    my_turtle.left(55)     #(a)
    my_turtle.backward(100)  #(a)
    my_turtle.forward(50)   #(a)
    my_turtle.left(55)     #(a)
    my_turtle.forward(50)    #(a)
    my_turtle.backward(50)  #(a)
    my_turtle.left(124)  #(a)
    my_turtle.forward(50)   #(a)

    my_turtle.left(150)    
    my_turtle.forward(100) 
    my_turtle.right(150)  
    my_turtle.forward(100) 
    my_turtle.left(150)
    my_turtle.forward(100) 
    my_turtle.right(9)
    my_turtle.left(150)

input()