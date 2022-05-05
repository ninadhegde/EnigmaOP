# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 02:45:11 2022

@author: ninad
"""

import turtle
import random

window = turtle.Screen() 
arthur = turtle. Turtle()
window.colormode (255)
arthur.speed (0)

arthur.width (2)

window.bgcolor (50,0,70) 
arthur.pencolor (50,255,90)

def shape (angle,side, limit): 
    reverseDirection = 200
    arthur. forward (side)

    if side %(reverseDirection* 2) == 0:
        angle = angle + 2

        print(side)
    elif side % reverseDirection == 0:
        angle = angle -2 
        print(side)

    arthur.right(angle)
    side = side + 2

    if side < limit:
        shape(angle,side, limit)

angle = 119
side = 0

limit= 800

shape (angle, side, limit)

turtle.done()