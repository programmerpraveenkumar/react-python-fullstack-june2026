# always input returns the string.
# value = input("enter the name")
# print(len(value))
# if len(value) >9 and len(value) <16:
#     print("name is valid")
# else:
#     print("name is not valid")

mobile = input("enter the mobile")
# print(len(value))
if not mobile.isdigit():
    print("Mobile is not valid")
elif len(mobile) <9  or len(mobile) >16:
     print("Mobile should be 10 to 15 chars")
else:
    print("Mobile is valid")

# print(type(value))
# length
# mobile no validation 10 to 15 chars
