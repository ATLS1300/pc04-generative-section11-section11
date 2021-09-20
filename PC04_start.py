"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Jade Singer

********* HEY, READ THIS FIRST **********

This is a description of the code that is written out below. This script is start code for PC04 + beyond. 
It imports random and math libraries along with the turtle libraries.
You should add your name(s), to line 4, and replace this description with one that describes what your code does!
(Hint: what patterns does it make? should it evoke any emotions?

"""
import turtle
import math
import random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
#Naming the turtle
sq1 = turtle.Turtle(shape="square")
sq2 = turtle.Turtle(shape="square")
sq3 = turtle.Turtle(shape="square")

#hiding the turtle
sq1.hideturtle()
sq2.hideturtle()
sq3.hideturtle()

#color lists
Caputmortuum = (86, 44, 44)
tuscany = (204, 153, 141)
seagreencrayola = (22, 244, 208)
cadetblue = (66, 158, 166)
indigodye = (21, 59, 80)
colorlist = [Caputmortuum, tuscany, seagreencrayola, cadetblue, indigodye]

#looping
sq1.penup()
for r in range (40):
    locationx = random.randint(-350,350) #random cordinates
    locationy = random.randint(-350,350)
    sq1.goto(locationx, locationy)
    sq1.color(random.choice(colorlist))  #random color
    sq1.shapesize(6,6) #size of square
    sq1.stamp()

#looping      
sq2.penup()    
for r in range (60):
    locationx = random.randint(-350,350) #random cordinates
    locationy = random.randint(-350,350)
    sq2.goto(locationx, locationy)
    sq2.color(random.choice(colorlist)) #random color
    sq2.shapesize(4,4) #size of square
    sq2.stamp()

#looping    
sq3.penup()
for r in range (40):
    locationx = random.randint(-350,350) #random cordinates
    locationy = random.randint(-350,350)
    sq3.goto(locationx, locationy)
    sq3.color(random.choice(colorlist))  #random color
    sq3.shapesize(2,2) #size of square
    sq3.stamp()
 
# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
