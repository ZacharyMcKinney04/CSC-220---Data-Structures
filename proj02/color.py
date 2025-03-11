class Color:
        def __init__(self):
                self._red = 0
                self._green = 0
                self._blue = 0

        def setRed(self, red):
                self._red = red

        def setBlue(self, blue):
                self._blue = blue

        def setGreen(self, green):
                self._green = green

        def getRed(self):
                return self._red

        def getBlue(self):
                return self._blue

        def getGreen(self):
                return self._green

        def SVG(self):
                return f"rgb({self._red}, {self._green}, {self._blue})"


#UNIT TESTING

if __name__ == "__main__":
    c = Color()
    print("getRed has")
    if (c.getRed() == 0):
    	print("passed")
    else:
        print("failed")
    print("getGreen has")
    if (c.getGreen() == 0):
        print("passed")
    else:
        print("failed")
    print("getBlue has")
    if (c.getBlue() == 0):
        print("passed")
    else:
        print("failed")

    print("setRed has")
    c.setRed(50)
    if (c.getRed() == 50):
        print("passed")
    else:
        print("failed")

    print("setGreen has")
    c.setGreen(70)
    if (c.getGreen() == 70):
        print("passed")
    else:
        print("failed")

    print("setBlue has")
    c.setBlue(30)
    if (c.getBlue() == 30):
        print("passed")
    else:
        print("failed")

    print("SVG function has")
    if (c.SVG() == "rgb(50, 70, 30)"):
        print("passed")
    else:
        print("failed")
        print(c.SVG())