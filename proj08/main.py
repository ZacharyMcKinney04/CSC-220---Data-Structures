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

from dictionary import Dictionary

stringDictionary = Dictionary()
stringDictionary.evaluateExpressions(textarea)

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Zachary McKinney
