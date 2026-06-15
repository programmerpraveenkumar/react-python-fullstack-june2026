# 
from abc import ABC, abstractmethod
class Animal(ABC):
    # abstract method should be defined  in child class
    @abstractmethod
    def printDetails(self):
        pass

class Lion(Animal):
#    def printDetails(self):
#        print("abstract method...")
   def hellow(self):
       print("some other ")

l = Lion()
# l.printDetails()