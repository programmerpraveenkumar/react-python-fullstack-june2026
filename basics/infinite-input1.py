# start with true
status = True
nameList = []
while status:
    name = input("enter the name.to exit enter exit ")
    if "exit" in name:
        status = False
        print("total names in the list ",len(nameList))
        print(nameList)
    else:
        if name not in nameList:
            nameList.append(name)
