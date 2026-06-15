# constructor is method will be called during the object creation
# syntax: __init__
class Bike:
    def __init__(self):
        print("this is constructor")

    def name_model(self,name):
        print(name)

bike_obj = Bike()
# bike_obj.name_model("bmw")