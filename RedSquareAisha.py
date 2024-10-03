import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed

# Define the side length of the square
side_length = 200 # Making sure i got four even sides 

# Set the fill colour to red
t.fillcolor("red")
t.begin_fill() # fill square in red, maybe I'll try purple next time

# Draw the square
for _ in range(4):
    t.forward(side_length)
    t.right(90)

# End the fill ( Ta-da! Red square check!)
t.end_fill()

# Write the name "Aisha" in the center
t.penup()
t.goto(-30, -10)  # Adjust the position based on the square size 
t.pendown()
t.color("white")  # Set the text color
t.write("Aisha", font=("Arial", 16, "bold")) # My name cuts off on the left upper corner and isn't in the middle. I think I did something wrong somewhere, maybe position?

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()
# There we go, a red square with half my name, not exactly what I wanted 
