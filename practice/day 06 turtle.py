#import turtle

#turtle.shape("turtle")  # triangle , square , arrow ,circle 모양을 입력하여 지정할 수 있다.
#turtle.bgcolor("tomato") # 다양한 색을 지정할 수 있다

# 사각형 그리기

#turtle.shape("arrow")

#turtle.forward(100) 
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)

# 삼각형 그리기
#t = turtle.Turtle()
#t.shape("turtle")
#t.forward(100)
#t.left(120)
#t.forward(100)
#t.left(120)
#t.forward(100)

# for사용 사각형그리기
#turtle.color("green")
#turtle.bgcolor("tomato")
#turtle.shape("turtle")
#
#for i in range(4) : # i 가 0,1,2,3까지 총 4번 반복
#    turtle.forward(100)
#    turtle.right(90)

# 반지름이 30인 원 그리기
from turtle import * # turtle을 import하고 전부 생략하겠다.
shape("turtle")
color("blue")
write("원 그리기 시작")
penup()
goto(100, 100) #goto 100, 100 >>> x축 100, y축 100 만큼 이동해라
pendown()
circle(30) #(a,b) a = 반지름을 의미

# 반복문으로 오각형 만들기 
# import turtle as t # turtle을 import 할 때 t 라는 변수에 저장한다.
# t.color("green")
# t.shape("turtle")
# t.bgcolor("tomato")
# 
# t.begin_fill()
# 
# for i in range(5) : # 0,1,2,3,4가 총 5번 반복
#     t.forward(100)
#     t.left(72)
# t.end_fill()

# set x, y 함수 이용예제
# import turtle
# t1 = turtle.Turtle()
# t1.shape("turtle")
# t1.color("blue")
# t1.setx(100) # x 좌표로 100만큼 가라
# 
# t2 = turtle.Turtle()
# t2.shape("turtle")
# t2.color("pink")
# t2.sety(100)

#RGB 스파이럴 그리기
from turtle import *
shape("turtle")
bgcolor("pink")

speed(0) # speed 0 일때가 가장 빠르다

colors = ['red' , 'green' , 'blue' , 'black']
pensize(2)
degree = 2 #각도

for i in range(1,300) : 
    pencolor(colors[i%4])
    forward(i)
    left(90 + degree)

mainloop() #터들명령어 종료 ?? 이거뭐임
input()

