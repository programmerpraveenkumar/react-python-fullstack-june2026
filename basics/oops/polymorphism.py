def printDetail(animal_obj):
    animal_obj.print()

class Lion:
    name="Lion"
    forestName = "african"
    def print(self ):
        print(self.name,self.forestName)

class Tiger:
    name="Tiger"
    forestName = "bengal"
    def print(self ):
        print(self.name,self.forestName)

printDetail(Lion())
printDetail(Tiger())