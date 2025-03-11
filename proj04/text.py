class Text:

	def __init__(self, words):
		self._words = words
		self._wordList = words.split(" ")
		self._wordList.sort()
		self._sortedList = self._wordList
		self._listSize = len(self._sortedList)
		self._first100 = self._sortedList[:100]

	def getAverageWordLength(self):
		letterSum = 0.0
		for word in self._wordList:
			letterSum += len(word)
		return (letterSum / self._listSize)

	def getListSize(self):
		return self._listSize

	def getFirst100(self):
		return self._first100

	def printGrid(self):
		endIdx = 10
		paragraph = ""
		for startIdx in range(0, len(self._first100), 10):
			paragraph += "<p>"
			endIdx = startIdx + 10
			paragraph += " ".join(self._wordList[startIdx:endIdx])
			paragraph += "</p><br>"
		return paragraph
