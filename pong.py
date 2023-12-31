import turtle

#call a window
window = turtle.Screen()
window.title("Pong by Sagar")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)#stops window from updating

#score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('black')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('black')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball

#Paddle A
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 20, 'normal'))


#run function
def paddle_a_up():
    y = paddle_a.ycor() 
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 20, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 20, 'normal'))

    # contact
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1