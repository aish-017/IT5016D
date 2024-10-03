import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")  # Set the drawing speed to the fastest

# Define the side length of the square
side_length = 200

# Set the fill colour to purple
t.fillcolor("purple") # Prepares to fill in square purple
t.begin_fill() 

# Draw the square
for _ in range(4): # Loop draws 4 sides of square
    t.forward(side_length) # moves turtle forward
    t.right(90) # Turns turtle 90 degrees for each side 

t.end_fill()

# Move to the center for the name
t.penup()
t.goto(0, 0)  # Go to the centre of the square
t.pendown()

# Write the name "Aisha" in black
t.color("black")
t.write("Aisha", align="centre", font=("Arial", 16, "bold")) # Displays Aisha in black, however I still cannot get my name to align to the centre 

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done() # We have a purple square, yet still unsuccessful in getting my name in the centre

