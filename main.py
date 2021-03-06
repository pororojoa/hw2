"""
This program draws a city skyline.
Authors: Davin Lim
Time spent: 5 hours
"""
import turtle    
wn = turtle.Screen()  
wildcat = turtle.Turtle() 

def pen_setup(x,y,z):
  wildcat.speed(10)
  wildcat.pensize(3)
  wildcat.penup()
  wildcat.goto(x,y)
  wildcat.pendown()
  wildcat.pencolor(z)

def direction_right(x,y):
  wildcat.right(x)
  wildcat.forward(y)
  
def direction_left(x,y):
  wildcat.left(x)
  wildcat.forward(y)

def draw_twintower():
 
  def draw_rooftop():
    direction_right(45,15)
    direction_right(90,15)
  
  pen_setup(-270, -150, 'green')
  direction_left(90,250)
  draw_rooftop()
  direction_right(45,50)
  direction_left(90,20)
  direction_left(90,50)
  draw_rooftop()
  direction_right(45,250)
  direction_right(90,20)
  direction_right(90,180)
  direction_left(90,20)
  direction_left(90,180)
  direction_right(90,20)

def draw_empirestate_building():
  wildcat = turtle.Turtle() 
  def pen_setup(x,y,z):
    wildcat.speed(9)
    wildcat.pensize(3)
    wildcat.penup()
    wildcat.goto(x,y)
    wildcat.pendown()
    wildcat.pencolor(z)
  pen_setup(-190, -150, 'grey')
  
  def direction_1(x,y):
    wildcat.left(90)
    wildcat.forward(x)
    wildcat.right(90)
    wildcat.forward(y)

  direction_1(20,20)
  direction_1(50,10)
  direction_1(25,10)
  direction_1(130,5)
  direction_1(15,20)
  direction_1(30,0)
  wildcat.left(90)
  wildcat.backward(30)
  wildcat.right(90)
  wildcat.forward(20)

  def direction_2(x,y):
    wildcat.right(90)
    wildcat.forward(x)
    wildcat.left(90)
    wildcat.forward(y)

  direction_2(15,5)
  direction_2(130,10)
  direction_2(25,10)
  direction_2(50,20)
  direction_2(20,0) 

def draw_slanted_building():
  wildcat = turtle.Turtle() 
  wildcat.speed(9)
  wildcat.pensize(3)
  wildcat.penup()
  wildcat.goto(-40,-150)
  wildcat.pendown()
  wildcat.pencolor('blue')
  
  def direction_right(x,y):
    wildcat.right(x)
    wildcat.forward(y)
  
  def direction_left(x,y):
    wildcat.left(x)
    wildcat.forward(y)
  
  direction_left(90,220)
  direction_right(135,40)
  direction_right(45,40)
  direction_left(45,40)
  direction_right(45,40)
  direction_left(45,40)
  direction_right(45,55)
  
def draw_inverted_slanted_building():
  wildcat = turtle.Turtle() 
  wildcat.speed(9)
  wildcat.pensize(3)
  wildcat.penup()
  wildcat.goto(66,-150)
  wildcat.pendown()
  wildcat.pencolor('red')

  def direction_right(x,y):
    wildcat.right(x)
    wildcat.forward(y)
  
  def direction_left(x,y):
    wildcat.left(x)
    wildcat.forward(y)

  direction_left(90,55)
  direction_left(45,40)
  direction_right(45,40)
  direction_left(45,40)
  direction_right(45,40)
  direction_left(45,45)
  direction_right(135,110)
  direction_right(90,223)

def draw_c_building():
  wildcat = turtle.Turtle() 
  wildcat.speed(9)
  wildcat.pensize(3)
  wildcat.penup()
  wildcat.goto(115,-150)
  wildcat.pendown()
  wildcat.pencolor('cyan')
  
  def direction_right(x,y):
    wildcat.right(x)
    wildcat.forward(y)
  
  def direction_left(x,y):
    wildcat.left(x)
    wildcat.forward(y)

  wildcat.forward(130)
  direction_left(90,40)
  direction_left(90,90)
  direction_right(90,130)
  direction_right(90,90)
  direction_left(90,40)
  direction_left(90,130)
  direction_left(90,210)

def draw_ground():
  wildcat = turtle.Turtle() 
  wildcat.speed(9)
  wildcat.pensize(3)
  wildcat.penup()
  wildcat.goto(-270, -150)
  wildcat.pendown()
  wildcat.forward(540)

def draw_sun():
  wildcat.speed(10)
  wildcat.pensize(0.5)
  wildcat.penup()
  wildcat.goto(150,130)
  wildcat.pendown()
  wildcat.color('orange','yellow')
  wildcat.begin_fill()
  while True:
	  wildcat.forward(50)
	  wildcat.left(165)
	  if abs(wildcat.pos()) < 0.5:
		  break
  wildcat.end_fill()
 
def draw_skyline():
  draw_twintower()
  draw_empirestate_building()
  draw_slanted_building()
  draw_inverted_slanted_building()
  draw_c_building()
  draw_ground()
  draw_sun()

draw_skyline()