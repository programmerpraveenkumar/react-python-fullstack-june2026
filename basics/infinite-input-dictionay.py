# start with true
status = True
# to define the empty dictionary
details = {}
while status:
    key = input("enter the key")
    value = input("enter the value or type exit to exit ")
    if "exit" in value:
        status = False
        # print("total names in the list ",len(nameList))
        # print(details)
        for v in details.values():
            print(v)
    else:
        if key in details:
            print("key is exist")
        else:
            details[key] = value

#### {}
# key and value
# key should not duplicate.if duplciate it will override  with new value
# items()-> to get the key,values from the dictionary
# keys()-> to get the keys from the dictionary
# values()-> to get the values from the dictionary
# in -> to check whether key is exist in the dictionary or not