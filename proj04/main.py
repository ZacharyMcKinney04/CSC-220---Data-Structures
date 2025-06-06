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

from text import Text

textSort = Text(textarea)

print(f'''<p>There are {textSort.getListSize()} words</p>''')
print(f'''<p> The average word length is {textSort.getAverageWordLength():.4f}</p>''')
#truncated float to 4 decimals as shown on slide 5 #.####
print("<br>")
print(textSort.printGrid())

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Zachary McKinney
# there is nothing below here!

