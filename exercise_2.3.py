import turtle as t

 

t.ht()
t.colormode(255)
t.pensize(3)

for r in range(40, 0, -10):

  for i in range(6):

    t.color(255, 165, r * 6)

    t.fillcolor(162, r * 6, 255)

    t.begin_fill()

    for _ in range(4):
        t.forward(r)
        t.right(90)

    t.end_fill()

    t.rt(60)

t.penup()
t.goto(0, -200)
t.pendown()

for r in range(40, 0, -10):

  for i in range(6):

    t.color(255, 165, r * 6)

    t.fillcolor(162, r * 6, 255)

    t.begin_fill()

    for _ in range(3):
        t.forward(r)
        t.left(120)

    t.end_fill()

    t.rt(60)