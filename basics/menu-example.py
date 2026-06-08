status = True
userlist = []
def addUser(name):
      userlist.append(name)

def displayAllUsers():
      for name in userlist:
        print(name)

def removeUser(name):
     userlist.remove(name)

while status:
    print("choose the option")
    print("1. add the value")
    print("2. list all the values")
    print("3. remove the value")
    print("4. exit")
    menu_num = input("Enter the menu number")
    if menu_num.isdigit():
            if menu_num == "1":
                name = input("enter the name to add")
                addUser(name)
            elif menu_num == "2":
                displayAllUsers()
            elif menu_num == "3":
                name = input("enter the name to remove")
                removeUser(name)
            else:
                print("you choose to exit")
                status = False
    else:
         print("plese choose proper menu option")
                  