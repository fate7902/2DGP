import turtle as t

def turtle_move(x,y): ## 위치 이동
    t.penup()
    t.goto(x,y)
    t.pendown()

t.title('거북이로  격자그리기!!')
t.shape('turtle')
t.pensize(3)
t.speed(0)

## 결과가 잘 보이도록 시작점 이동
turtle_move(-300,-300)
(x,y) = t.position()

for i in range(0,6):
    turtle_move(x,y+100*i)
    t.setheading(0)
    t.forward(500)
    turtle_move(x+100*i,y)
    t.setheading(90)
    t.forward(500)

t.exitonclick()