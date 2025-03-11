#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

print ("textbox contains <b>{}</b> <br>".format( textbox ))
print ("textarea contains <b>{}</b> <br>".format( textarea ))


from point import Point
from color import Color
from circle import Circle
import random

# code that creates 1000 or so objects and puts them in circle_list
# that code will generate Point and Color objects to build the circles
circles = []
for count in range(0,1000):
        circ = Circle()
        p = Point()
        coordinate_value = random.randint(0, 1000)
        p.setAcross(coordinate_value)
        coordinate_value = random.randint(0, 1000)
        p.setDown(coordinate_value)
        circ.setCenter(p)
        random_color = Color()
        rgb_value = random.randint(0, 255)
        random_color.setRed(rgb_value)
        rgb_value = random.randint(0, 255)
        random_color.setGreen(rgb_value)
        rgb_value = random.randint(0, 255)
        random_color.setBlue(rgb_value)
        circ.setFill(random_color)
        random_radius = random.randint(0,10)
        circ.setRadius(random_radius)
        circles.append(circ)

# put code here to generate a random circle and add it to the list.

print ('<svg height="1000" width="1000">')   #single SVG canvas
for circle in circles:
    print (circle.SVG()) # or something similar
print ('</svg>')    



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Zachary McKinney 
# there is nothing below here!





