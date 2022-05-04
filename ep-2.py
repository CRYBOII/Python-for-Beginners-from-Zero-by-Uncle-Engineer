import turtle
import time


tao = turtle.Pen()
tao.shape("turtle")



def Rectangle():
    for i in range(22):
        tao.forward(40)
        tao.left(90)
        tao.forward(40)
        tao.left(10)

        

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(200,200)
Rectangle()

time.sleep(5)