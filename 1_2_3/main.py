#   a123_apple_1.py
import turtle as trtl
import random as rand
import time as time 

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
alphabetti = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
die = rand.randrange(len(alphabetti))
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
drawer = trtl.Turtle()
apple = trtl.Turtle()

def v():
  drawer.penup()
  drawer.goto(-30,95)
  drawer.pendown()
  drawer.color("white")
  drawer.write(alphabetti[die], font=("Comic Sans MS", 50, "bold")) 
  drawer.hideturtle()

  #-----functions-----
  # given a turtle, set that turtle to be shaped by the image file
  def draw_apple(active_apple):
    active_apple.shape(apple_image)
    apple.penup()
    apple.hideturtle()
    apple.goto(rand.randint(-150,150),rand.randint(-150,100))
    apple.showturtle()
    wn.update()

  def drop_apple():
    apple.penup()
    apple.goto(apple.xcor(),-150)
    drawer.clear()
    drawer.hideturtle()


  #-----function calls-----
  draw_apple(apple)
  wn.bgpic("background.gif")
  wn.onkeypress(drop_apple,alphabetti[die])
  wn.listen()

for i in range(10):
  time.sleep(1.5)
  die = rand.randrange(len(alphabetti))
  drawer.clear()
  v()

