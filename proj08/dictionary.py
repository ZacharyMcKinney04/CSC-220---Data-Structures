class Dictionary:

  def __init__(self):
    self._dictionary = {}

  def evaluateExpressions(self, expressions):
    expression_list = expressions.split("\n")
    for expression in expression_list:
      parts = expression.split("<-")
      var = parts[0].strip()
      if var == "DUMP":
        self._printDump()
      elif var == "NAME":
        self._printName()
      elif var == "":
        #empty line given
        continue 
      elif len(parts) <= 1:
        raise SyntaxError(f'{var}')
      else:
        val = parts[1].strip()
        self.processVal(var, val)


  def processVal(self, var, val):
      if val[0].islower(): #check if lowercase letter
        if val not in self._dictionary:
            raise LookupError(f'Error: {val} not defined')
        else:
            self._dictionary[var] = self._dictionary[val]
      elif val[0] in "0123456789":
        self._dictionary[var] = float(val)
      else:
        raise SyntaxError(f'{var}')

  def _printName(self):
    print("zmckinney1")

  def _printDump(self):
    print("<p>Printing all variables:</p>")
    for var in self._dictionary:
      print(f"<p>{var} {self._dictionary[var]}</p>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Zachary McKinney
