import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed

# Define the side length of the square
side_length = 200

# Set the fill color to red
t.fillcolor("red")
t.begin_fill()

# Draw the square
for _ in range(4):
    t.forward(side_length)
    t.right(90)

# End the fill
t.end_fill()

# Write the name "Aisha" in the center
t.penup()
t.goto(-30, -10)  # Adjust the position based on the square size
t.pendown()
t.color("white")  # Set the text color
t.write("Aisha", font=("Arial", 16, "bold"))

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()
