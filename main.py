from turtle import Screen, Turtle
import random


is_race_on = False
screen = Screen()
screen.setup(width=800, height=710)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "orange", "green", "blue", "purple", "black", "brown", "coral", "khaki",
          "magenta", "tomato", "indigo", "olive", "pink", "peru", "lime", "aquamarine", "navy",
          "lime green", "crimson", "maroon"]
all_turtles = []


y_val = -310
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-370, y=y_val)
    new_turtle.speed("fastest")
    y_val += 30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 360:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won!")
            else:
                print(f"You've lost! The {winning_color} turtle won!")

        random_distance = random.randint(0, 25)
        turtle.forward(random_distance)


screen.exitonclick()