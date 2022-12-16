import turtle
s = turtle.Screen()
t = turtle.Turtle()
# t.shape("turtle")
s.bgcolor("gray")
t.pensize(10)
t.color("pink")

#J857A
t.penup()
t.goto(-300,0)
t.pendown()
t.right(90)
t.circle(45,180)
t.forward(100)
t.left(90)
t.forward(50)

#8
t.penup()
t.goto(-150,30)
t.pendown()
t.circle(30)
t.left(180)
t.circle(30)

#5
t.penup()
t.goto(-95,-30)
t.pendown()
t.circle(40,180)
t.right(90)
t.forward(50)
t.right(90)
t.forward(40)

#7
t.penup()
t.goto(-30,-30)
t.pendown()
t.left(65)
t.forward(140)
t.left(115)
t.forward(65)

#A
t.penup()
t.goto(10,-30)
t.pendown()
t.right(180)
t.left(65)
t.forward(140)
t.right(130)
t.forward(140)
t.left(180)
t.penup()
t.forward(70)
t.pendown()
t.left(65)
t.forward(60)

t.penup()
t.goto(100,-30)
t.pendown()




s.exitonclick()
