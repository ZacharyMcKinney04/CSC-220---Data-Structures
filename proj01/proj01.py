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

def print_left_circle():
        print('<circle cx="300" cy="50" r="40" stroke="red" stroke-width="10" fill="white" />')

def print_right_circle():
         print('<circle cx="700" cy="50" r="40" stroke="green" stroke-width="1" fill="white" />')

def print_rectangle():
         print('<rect width="200" height="100" x="400" y="0" rx="1" ry="1" fill="blue" opacity=".5" />')

def print_name():
         print('<text x="410" y="55" font-size="20" fill="black">Zachary McKinney</text>')

print ('<svg height="1000" width="1000" style="display:block; margin:auto;">')
print_left_circle()
print_rectangle()
print_right_circle()
print_name()
print ('</svg>')

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Zachary McKinney
# there is nothing below here!

