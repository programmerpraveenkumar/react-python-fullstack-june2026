value = input("enter the name")

# value shuld have either mr or miss
#  check whether value is exist or not in the string using match operator
if "mr" in value or "miss" in value:
    print("yes its exist")
else:
    print("your name is wrong ",value)
