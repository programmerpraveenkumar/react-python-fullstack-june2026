firstname = "hari"
lastname = "haran"
age = 35
name = firstname+" "+lastname
# detail = "hi "+firstname+" "+lastname+" and his age is "+str(age)
detail = f"hi {firstname} {lastname} and his age is {age}"
print(detail)
print(name)
# format string-> f"as;dfjasdfasdflakjdf;asdjf;ajsf;dj{vairable}"
def printAnimalDetails(animal_name,forest_name,count):
    print(f"animal name is {animal_name} living in {forest_name}.count is {count}")
    
printAnimalDetails("lion","africa",67)
printAnimalDetails("tiger","bengal",100)
printAnimalDetails("elephant","amazon",55)