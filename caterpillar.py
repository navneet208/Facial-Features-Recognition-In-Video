import turtle as tu
import time
import random


game_started = False
tu.bgcolor("light blue")

#We need 4 turtles
caterpillar = tu.Turtle()
caterpillar.shape("square")
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = tu.Turtle();
#definign coordinates for leaf's shape
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
#Since we've defined a new shape, we need to register it.
tu.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color("green")
leaf.penup()
leaf.speed()
leaf.hideturtle()

text_turtle = False
text_turtle = tu.Turtle();
text_turtle.write("Press space to Begin", align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = tu.Turtle();
score_turtle.hideturtle()
score_turtle.speed(0)


#Defining Functions:
def outside_window():
    left_wall = -tu.window_width() / 2
    right_wall = tu.window_width() / 2
    top_wall = tu.window_height() / 2
    bottom_wall = -tu.window_height() / 2
    (x,y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    #outside will be TRUE if any of the condition satisfies.
    return outside

def place_leaf():
    leaf.hideturtle()
    #randomly placing leaf on window_width
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.showturtle()


def game_over():
    caterpillar.color("light blue")
    leaf.color("light blue")
    tu.penup()
    tu.hideturtle()
    tu.write(" G A M E  O V E R !!", align='center', font=('Aerial', 25, 'normal'))


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (tu.window_width()/2) -50
    y = (tu.window_height()/2) -50 #for padding
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align = 'right', font=('Aerial', 30, 'bold'))

#main calling function

def start_game():
    #definig a global variable
    global game_started
    if game_started:
        return
    game_started = True
    score = 0

    text_turtle.clear()


    #caterpillar
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while(True):
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length+= 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed+= 1
            score+= 10
            display_score(score)
        if outside_window():
            game_over()
            break


def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)


#start_game()
#KEYSS>>>>>>>>>>>>>>>>>>>>>>>>>>>
#game_started = False
tu.onkey(start_game, 'space')
tu.onkey(move_up, 'Up')
tu.onkey(move_down, 'Down')
tu.onkey(move_left, 'Left')
tu.onkey(move_right, 'Right')
tu.listen()
tu.mainloop()

#start_game()




time.sleep(3)
