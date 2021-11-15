#   a123_apple_1.py
import turtle as trtl

#-----setup-----
pear_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file
drawer = trtl.Turtle()
apple = trtl.Turtle()

drawer.penup()
drawer.goto(-30,95)
drawer.pendown()
drawer.color("white")
drawer.write("A", font=("Comic Sans MS", 74, "bold")) 
drawer.hideturtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(pear_image)
  wn.update()
  
def drop_apple():
  apple.penup()
  apple.goto(apple.xcor(),-150)
  drawer.clear()
  drawer.hideturtle()



#-----function calls-----
draw_apple(apple)
wn.bgpic("background.gif")
wn.onkeypress(drop_apple,"a")
wn.listen()
wn.mainloop()