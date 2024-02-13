import turtle

def draw_flower():
    flower_turtle = turtle.Turtle()
    flower_turtle.shape("turtle")
    flower_turtle.color("red")
    flower_turtle.speed(10)  # Increase speed

    # Draw flower petals
    for _ in range(36):
        flower_turtle.forward(100)
        flower_turtle.right(45)
        flower_turtle.forward(100)
        flower_turtle.right(135)
        flower_turtle.forward(100)
        flower_turtle.right(45)
        flower_turtle.forward(100)
        flower_turtle.right(135)

        flower_turtle.right(10)  # Move to the next petal

    # Draw flower center
    flower_turtle.color("yellow")
    flower_turtle.dot(50)

    flower_turtle.hideturtle()

def draw_bunch_of_flowers(num_flowers):
    window = turtle.Screen()
    window.bgcolor("white")

    turtle.speed(10)  # Increase speed

    for _ in range(num_flowers):
        draw_flower()
        turtle.penup()
        turtle.goto(turtle.xcor() + 200, turtle.ycor())  # Move to the next position

    window.exitonclick()

# Call the function to draw a bunch of flowers
draw_bunch_of_flowers(5)
