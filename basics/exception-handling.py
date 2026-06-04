try:
    x = "t54545"
    y = int(x)#error as it is not number
except Exception as e:
    print(e)
else:
    # will work only when try is success,
    #if try is failure this will not work
    print("all success")    
finally:
    # irrespective of try or catch finally will work
    print("always executed")

print("this is the last line")