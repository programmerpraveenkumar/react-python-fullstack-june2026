# class Person-> name,address,mobile
# class Ashok-> printDetails()

class Person:
    name="adfads"
    address="adsfds"
    mobile=5665

class Ashok(Person):
    def printDetails():
        print("sampel details")

class Arun(Person):
    def printDetails():
        print("sampel details")


ashok_obj = Ashok()
ashok_obj.mobile = 85858
print(ashok_obj.address)

arun_obj = Arun()
arun_obj.mobile = 96548
print(arun_obj.mobile)