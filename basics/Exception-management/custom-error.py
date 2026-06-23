try:
    age = 33
    if age >10:
        raise ValueError("app can be acccess only by children")
    else:
        print('you r child so can access')

except Exception as e:
    print("Error",e)
print("this is last line")