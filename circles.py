#!/usr/bin/env python3

# File name: circles.py
# Description: Simple Tk program that draws randomly colored circles
# Author: Sean McGroty
# Date created: 11/27/2021
# Date last modified: 11/27/2021
# Version: 0.001
# License: MIT

import random
import time
import tkinter
import tkinter.filedialog as fd

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
DEFAULT_DELAY = 1
DEFAULT_MAXRADIUS = 50

def save_canvas(*args):
    file = fd.asksaveasfile(initialfile="image.eps", defaultextension=".eps", filetypes=[("Encapsulated PostScript File","*.eps")])
    image = C.postscript()
    file.write(image)

def create_circle(canvas, x, y, radius, color):
    x0 = x-radius
    y0 = y-radius
    x1 = x+radius
    y1 = y+radius
    
    return canvas.create_oval(x0,y0,x1,y1,fill=color,outline=color)
    
def random_color():
    red = random.randrange(0,65535)
    green = random.randrange(0,65535)
    blue  = random.randrange(0,65535)
    
    return "#{:04x}{:04x}{:04x}".format(red, green, blue)

def draw_random_circle():
    color = random_color()
    x = random.randrange(0, CANVAS_WIDTH)
    y = random.randrange(0, CANVAS_HEIGHT)
    radius = random.randrange(0, int(maxradius.get()))
    create_circle(C,x,y,radius,color)
    
top = tkinter.Tk()
top.title("Draw circles (double-click to save)")

maxradius_label = tkinter.Label(top, text="Max radius")
maxradius_label.pack()
maxradius = tkinter.StringVar(top, DEFAULT_MAXRADIUS)
#radius.trace('w', update_radius)
maxradius_box = tkinter.Entry(top, bd=5, textvariable=maxradius)
maxradius_box.pack()

delay_label = tkinter.Label(top, text="Delay seconds")
delay_label.pack()
delay = tkinter.StringVar(top, DEFAULT_DELAY)
#delay.trace('w', update_delay)
delay_box = tkinter.Entry(top, bd=5, textvariable=delay)
delay_box.pack()

C = tkinter.Canvas(top, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
C.pack()
C.bind("<Double-1>", save_canvas)

while True:
    draw_random_circle()
    top.update()
    time.sleep(float(delay.get()))
