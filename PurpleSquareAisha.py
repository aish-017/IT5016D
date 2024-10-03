import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed to the fastest

# Define the side length of the square
side_length = 200

# Set the fill color to purple
t.fillcolor("purple")
t.begin_fill()

# Draw the square
for _ in range(4):
    t.forward(side_length)
    t.right(90)

t.end_fill()

# Move to the center for the name
t.penup()
t.goto(0, 0)  # Go to the center of the square
t.pendown()

# Write the name "Aisha" in black
t.color("black")
t.write("Aisha", align="center", font=("Arial", 16, "bold"))

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()

