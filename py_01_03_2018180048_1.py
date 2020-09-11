import turtle as t

def turtle_move(x,y): ## 위치 이동
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)

def draw_ba(x,y): ## ㅂ 그리기
    t.setheading(-90)
    t.forward(100)
    t.setheading(0)
    t.forward(75)
    t.setheading(90)
    t.forward(100)
    turtle_move(x,y-50)
    t.forward(75)

def draw_a(section,x,y): ## ㅇ,ㅏ 그리기
    if section == 1: ## ㅇ 그리기
        turtle_move(x+32,y-75)
        t.circle(36)
    else : ## ㅏ 그리기
        turtle_move(x+100,y+25)
        t.setheading(-90)
        t.forward(150)
        turtle_move(x+100,y-50)
        t.forward(50)

def draw_ga(section,x,y): ## ㄱ 그리기
    if section == 1: ## 초성일 경우
        pass
    else : ## 종성일 경우
        turtle_move(x,y-150)
        t.forward(100)
        t.setheading(-90)
        t.forward(50)

def draw_ui(x,y): ## ㅢ 그리기
    turtle_move(x-25,y-100)
    t.forward(125)
    turtle_move(x+100, y)
    t.setheading(-90)
    t.forward(125)

def draw_e(x,y): ## ㅣ 그리기
    turtle_move(x+100, y)
    t.setheading(-90)
    t.forward(100)

def draw_na(section,x,y): ## ㄴ 그리기
    if section == 1: ## 초성일 경우
        pass
    else : ## 종성일 경우
        turtle_move(x+15, y-100)
        t.setheading(-90)
        t.forward(50)
        t.setheading(0)
        t.forward(100)

t.title('거북이로 이름쓰기!!')
t.shape('turtle')
t.pensize(3)
t.speed(0)

## 박 그리기
turtle_move(-200,200)
(x,y) = t.position()
draw_ba(x,y)
draw_a(2,x,y)
draw_ga(2,x,y)

## 의 그리기
turtle_move(0,200)
(x,y) = t.position()
draw_a(1,x,y)
draw_ui(x,y)

## 인 그리기
turtle_move(200,200)
(x,y) = t.position()
draw_a(1,x,y)
draw_e(x,y)
draw_na(2,x,y)

t.exitonclick()