"""turtle art"""
from .turtle import Turtle 
from math import pi 
from random import random 

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi /180.0 #Constant 

def main () -> None: ...
    

def click (x: float, y: float) -> Turtle:
    """Moves turtle where ever you click"""
    t: Turtle = Turtle ()
    t.setSpeed(0.25)
    t.moveTo(x,y)

    t.forward (150)
    t.left(pi/2.0)

    t.forward (140)
    t.left(pi/2.0)
    
    #code to paint a flower 
   # length: float = 150.0
    #while length > 0.0: 
       # t.forward(length)
       # t.left(pi/2.0-pi/8.0)
       # length -= 2.0 
       
    branch (t, y * 0.15 , 90 * DEGREE)
    return t 

def branch (t: Turtle, length: float, angle: float ) -> None: 
    t.turnTo(angle)
    t.forward(length)
    if length > 3.0: 
        branch(t,length * 0.75, angle + 35.0 * DEGREE)
        branch(t, length * 0.75, angle - 35.0 * DEGREE )
    t.turnTo(angle+pi)
    t.forward(length)

   