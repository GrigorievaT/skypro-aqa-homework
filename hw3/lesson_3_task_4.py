#Рисуем собаку
from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

def draw_rect(t): #рисуем восьмиугольник - голова
    for x in range(0, 6):
        t.forward(60)
        t.left(60)

draw_rect(my_turtle)
my_turtle.up() # рисуем нос
my_turtle.goto(30, 30)
my_turtle.down()
my_turtle.circle(8)

#рисуем глаза
my_turtle.up() 
my_turtle.goto(10, 60)
my_turtle.down()
my_turtle.circle(5)
my_turtle.up()
my_turtle.goto(50, 60)
my_turtle.down()
my_turtle.circle(5)

#Ухо левое
my_turtle.up() 
my_turtle.goto(0, 105)
my_turtle.down()
my_turtle.backward(50)
my_turtle.left(45)
my_turtle.backward(60)
my_turtle.left(45)
my_turtle.backward(30)
my_turtle.left(90)
my_turtle.backward(40)
my_turtle.left(45)
my_turtle.backward(40)
#Ухо правое
my_turtle.up() 
my_turtle.goto(60, 105)
my_turtle.down()
my_turtle.left(135)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(60)
my_turtle.right(45)
my_turtle.forward(30)
my_turtle.right(90)
my_turtle.forward(40)
my_turtle.right(45)
my_turtle.forward(40)
#Туловище
my_turtle.up() 
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.left(90)
my_turtle.forward(60)
my_turtle.left(45)
my_turtle.forward(60)
my_turtle.right(45)
my_turtle.forward(60)
my_turtle.left(90)
my_turtle.forward(80)
my_turtle.left(45)
my_turtle.forward(120)
my_turtle.left(45)
my_turtle.forward(80)
my_turtle.left(90)
my_turtle.forward(60)
my_turtle.right(45)
my_turtle.forward(60)
my_turtle.left(45)
my_turtle.forward(60)
#Лапы
my_turtle.up() 
my_turtle.goto(0, -100)
my_turtle.down()
my_turtle.left(135)
my_turtle.forward(70)
my_turtle.up() 
my_turtle.goto(30, -100)
my_turtle.down()
my_turtle.forward(100)
my_turtle.up() 
my_turtle.goto(60, -100)
my_turtle.down()
my_turtle.forward(70)
my_turtle.up() 
my_turtle.goto(-30, -200)
my_turtle.down()
my_turtle.left(180)
my_turtle.circle(-30, 180)
my_turtle.right(180)
my_turtle.circle(-30, 180)
#Хвост
my_turtle.up() 
my_turtle.goto(-30, -200)
my_turtle.down()
my_turtle.right(90)
my_turtle.forward(60)
my_turtle.right(45)
my_turtle.forward(80)
my_turtle.right(45)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.forward(85)
my_turtle.right(135)
my_turtle.forward(163)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()
