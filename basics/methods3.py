# i have list inside a function
# check element is eixist or not.
# if exist return exist
# else return not exist

def checkExist(ele):
    list=[1,2,3,4,5]
    if ele in list:
        return "exist"
    else:
        return "not exist"
result = checkExist(12)
print(result)
