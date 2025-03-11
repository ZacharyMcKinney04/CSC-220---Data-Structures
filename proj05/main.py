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

print("<br>")

def extract_ints(string):
  string_list = string.split()
  int_list = []
  for split in string_list:
    int_list.append(int(split))
  return int_list

def get_path(int_list):
  visited_list = []
  path_list = []
  can_win = path_can_win(0, int_list, path_list, visited_list)
  if (can_win):
    path_list = path_list[::-1]
  print(visited_list)
  return path_list

def path_can_win(idx, int_list, path_list, visited_list):
  #base cases
  if idx >= len(int_list):
    return False
  if idx < 0:
    return False
  if idx in visited_list:
    return False
  if idx == len(int_list) - 1:
    path_list.append(idx)
    return True
  if int_list[idx] == 0:
    #must check after checking if it's the last index
    return False
  #setup for checking
  visited_list.append(idx)
  #check left and right paths
  idx_add = int_list[idx]
  if (path_can_win(idx - idx_add, int_list, path_list, visited_list)):
    path_list.append(idx)
    return True
  if (path_can_win(idx + idx_add, int_list, path_list, visited_list)):
    path_list.append(idx)
    return True
  return False

string = textbox

numbers = extract_ints(string)
path = get_path(numbers)
if len(path) == 0:
	print("<p>Could not find a path with textbox numbers</p>")
else:
	print("<p>Got winning path from textbox numbers</p>")
	formatted_string = "<p>"
	for num in path:
		formatted_string += (f"{num}->")
	formatted_string += ("win</p>")
	print(formatted_string)

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Zachary McKinney
