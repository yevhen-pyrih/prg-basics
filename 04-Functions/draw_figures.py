import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle


# Side length
side_length = 100

figures.draw_square(side_length)

figures.move_to(100, -100)

figures.draw_triangle(side_length)

figures.move_to(-100, 100)


figures.draw_rectangle(100, 200)

window.mainloop()