# open the file
# w->will replace the content if file exists
# a->will add the content if file exists
with open("sample.txt","w") as myfile:
    myfile.write("this is new content")