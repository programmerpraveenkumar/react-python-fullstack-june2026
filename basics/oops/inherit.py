class Animal:
    def printDetails(self,name,forestname):
        print(name,forestname)
# inheritance the animal to lion
class Lion(Animal):
    name="Lion"
    forestName = "african"
    def print(self ):
        self.printDetails(self.name,self.forestName)
# inheritance the animal to Tiger
class Tiger(Animal):
    name="Tiger"
    forestName = "bengal"
    def print(self ):
        self.printDetails(self.name,self.forestName)


lion = Lion()
lion.print()

