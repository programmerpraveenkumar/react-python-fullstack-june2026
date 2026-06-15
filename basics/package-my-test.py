# # import the functon from another package
# foldername and file import the function
from mypackage.myfunctions import addition
from mypackage2.anotherfunction import printName

# from mypackage import addition


result = addition(4,5)

print(result)

printName("hi  this is anoth file")