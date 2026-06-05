# start with true
status = True
while status:
    name = input("enter the name.to exit enter exit ")
    if "exit" in name:
        print("you enter exit.so we are closing..")
        # changing the status as false .
        status = False
    else:
        print("you enterd is ",name)