class Point:

	def __init__(self):
		self._across = 0
		self._down = 0

	def getAcross(self):
		return self._across

	def getDown(self):
		return self._down

	def setAcross(self, x):
		self._across = x

	def setDown(self, y):
		self._down = y


#UNIT TESTING

if __name__ == "__main__":
    p = Point()
    if (p.getAcross() == 0):
    	print("getAcross works")
    else:
    	print("getAcross Failed")

    if (p.getDown() == 0):
    	print("getDown works")
    else:
    	print("getDown Failed")

    p.setAcross(5)
    if (p.getAcross() == 5):
    	print("setAcross works")
    else:
    	print("setAcross Failed")

    p.setDown(3)
    if (p.getDown() == 3):
    	print("setDown works")
    else:
    	print("setDown Failed")
