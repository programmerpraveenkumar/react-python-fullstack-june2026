# hiding the variable from accessing
# getter method -> get  the value for the variable
# setter method -> set the value to the varible
class Country:
    def __init__(self):
       self.__name = None
       
    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    

country_obj = Country()
country_obj.setName("dubai")
print(country_obj.getName())