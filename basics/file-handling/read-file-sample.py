# open the file

try:
    with open("mydetails.txt","r") as myfile:
        #for loop will run till the last line
        for line in myfile:
             print(line)
except Exception as e:
    print(e)