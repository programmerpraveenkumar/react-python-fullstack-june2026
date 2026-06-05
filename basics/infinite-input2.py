# start with true
status = True
# to define the empty set
nameList  = set()
while status:
    # exittrsdfsdf
    name = input("enter the name.to exit enter exit ")
    if "exit" in name:
        status = False
        print("total names in the list ",len(nameList))
        print(nameList)
    else:
        # duplicate will be ignored 
        nameList.add(name)
 