class Car:
    name=None
    price=None

class Benz(Car):
    def printDetails(self,name,price):
        # assign the parameter to the variables
        # variables coming from parent class
        self.name = name
        self.price = price
        print(self.name,self.price)

# to access the class
benz= Benz()
benz.printDetails("benz",1000)
    

