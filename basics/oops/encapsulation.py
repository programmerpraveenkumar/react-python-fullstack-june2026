class Person:
	def __init__(self):
		self.__name = None


	def setName(self,name):
		self.__name = name
    
	def getName(self):
		return self.__name
	
personObj = Person()
personObj.setName("adsfd")
print(personObj.getName())