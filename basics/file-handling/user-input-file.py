name = input("enter your name")
mobile = input("enter your mobile")
address = input("enter your address")
# \n
with open("mydetails.txt","w") as myfile:
	myfile.write(name+"-"+mobile+"-"+address)