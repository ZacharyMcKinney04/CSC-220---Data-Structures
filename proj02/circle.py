from point import Point
from color import Color

class Circle:
	def __init__(self, center = None, radius = 1, fill = None):
		if center is None:
			self._center = Point()
		else:
			self._center = center
		if fill is None:
			self._fill = Color()
		else:
			self._fill = fill
		self._radius = radius

	def SVG(self):
		return f'''<circle r="{self._radius}" cx="{self._center.getAcross()}" cy="{self._center.getDown()}" fill="{self._fill.SVG()}"/>'''

	def getCenter(self):
		return self._center

	def getRadius(self):
		return self._radius

	def getFill(self):
		return self._fill

	def setCenter(self, center2):
		self._center = center2

	def setRadius(self, radius):
		self._radius = radius

	def setFill(self, fill):
		self._fill = fill

#UNIT TESTING
if __name__ == "__main__":
    circ = Circle(Point(), 1, Color())

    print("getCenter has ")
    if (circ.getCenter().getAcross() == 0 and circ.getCenter().getDown() == 0):
        print("passed")
    else:
        print("failed")

    print("getRadius has")
    if (circ.getRadius() == 1):
        print("passed")
    else:
        print("failed")

    print("getFill has")
    if (circ.getFill().getRed() == 0 and circ.getFill().getGreen() == 0 and circ.getFill().getBlue() == 0):
        print("passed")
    else:
        print("failed")

    new_cent = Point()
    new_cent.setAcross(5)
    new_cent.setDown(3)
    circ.setCenter(new_cent)
    print("setCenter has")
    if (circ.getCenter().getAcross() == 5 and circ.getCenter().getDown() == 3):
        print("passed")
    else:
        print("failed")

    circ.setRadius(9)
    print("setRadius has")
    if (circ.getRadius() == 9):
        print("passed")
    else:
        print("failed")

    c2 = Color()
    c2.setRed(21)
    c2.setGreen(32)
    c2.setBlue(43)
    circ.setFill(c2)
    print("setFill has")
    if(circ.getFill().getRed() == 21 and circ.getFill().getGreen() == 32 and circ.getFill().getBlue() == 43):
        print("passed")
    else:
        print("failed")

    svg_txt = circ.SVG()
    print("SVG has")
    if (svg_txt == """<circle r="9" cx="5" cy="3" fill="rgb(21, 32, 43)"/>"""):
        print("passed")
    else:
        print("failed")
        print(circ.SVG())
