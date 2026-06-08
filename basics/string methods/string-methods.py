name = "hihariharan787"
# only first char will be in capital
print(name.capitalize())

# count the occur of character in the string
print(name.count('c'))

# to check whether first char match
print(name.startswith("a"))

# will check the last char match
print(name.endswith("cn"))

print(name.index("i"))
print(name.find("a"))

# check for only text and number
# if space or special char will return the false
print(" isalnum ",name.isalnum())

name = "hihello"
# to check only for alpha(text)
# will be false if text contains special chars or space or number
print(name.isalpha())
price = "89"
# to check only for the numbers
print(price.isdecimal())
name = "hari haran hi how are you"
new_name = name.split("how")
print(new_name)
# multi_lines = """
# hi how are you
# this is also fine
# i came for business meeeting
# """
multi_lines = "hi how are you\nthis is also fine\ni came for business meeeting"
# split the lines with \n
print(multi_lines.splitlines())
