# recv two number,add the params,
# if the resut is even return as even or dont return.
# # definition,name,parmeter,logic,return,calling
# def add(a,b):
#     result = a+b
#     print(result)
#     # return the result
#     return result

# # calling the function
# result = add(4,5)
# print(result)`
# 

def checkEven(a,b):
    result = a+b
    if result % 2 == 0:
        return "even"
    print("this is odd.so no return")

result = checkEven(10,10)
print(result)
    