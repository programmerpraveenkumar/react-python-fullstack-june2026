try:
    list=["u","p","o"]
    # pass 8 to 15
    password = input("enter password")
    print(list[1])
    if len(password)>15 or len(password)<8:
        raise ValueError("password shuld be 8 to 15..")
    else:
        print("password is ok")
except IndexError as e:
        print("Index error occured!!!",e)
except Exception as e:
    print("Common error occured!!!",e)
finally:
     print("finaly")

