# hiding the variable from accessing

class City:
    # constructor
    def __init__(self):
        # define the private variables using `__`
        self.__name = None
        self.__people_count = None

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setPeopleCount(self,count):
        self.__people_count = count

    def getPeopleCount(self):
        return self.__people_count
    
city_obj = City()
city_obj.setName("city1")
city_obj.setPeopleCount("1500")
print(city_obj.getName())
print(city_obj.getPeopleCount())