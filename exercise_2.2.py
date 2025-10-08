import turtle as t

# три круга
t.penup()
t.goto(-150, 100)
t.pendown()


for i in range(3):
    t.begin_fill()
    t.color(40+50*i, 0, 40+50*i)
    t.circle(30+20*i)
    t.end_fill()
    t.penup()
    t.forward(150)
    t.pendown()

# прямоугольник
t.penup()
t.goto(-300, -50)
t.pendown()
t.begin_fill()
t.color("skyblue")
for _ in range(2):
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

# ромб
t.penup()
t.goto(-100, -50)
t.pendown()
t.begin_fill()
t.color("lightgreen")
for _ in range(2):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
t.end_fill()

# трапеция
t.penup()
t.goto(150, -50)
t.pendown()
t.begin_fill()
t.color("violet")
t.forward(140)
t.right(120)
t.forward(60)
t.right(60)
t.forward(80)
t.right(60)
t.forward(60)
t.right(120)
t.end_fill()

# елка
t.penup()
t.goto(-30, -350)
t.pendown()
t.color("green")

for i in range(3):
    t.begin_fill()
    for _ in range(3):

        t.forward(100 - i*20)
        t.left(120)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(((100 - i*20)-(100 - (i+1)*20))/2)
    t.pendown()

# три квадрата
t.penup()
t.goto(-200, -300)
t.pendown()
for i in range(3):
    t.begin_fill()
    t.color("gold")
    for _ in range(4):
        t.forward(30)
        t.right(90)
    t.end_fill()
    t.penup()
    t.forward(60)
    t.pendown()
