class Animal:
   name="lion"
   count=45
   forest="Africa"

# lion is inheritated from animal class
# all props from  animal wil be exist in the lion also internally
class Lion(Animal):
	def printDetails():
		print("this is from lion class.")
	
#object creation
lion_obj = Lion()
print(lion_obj.forest)