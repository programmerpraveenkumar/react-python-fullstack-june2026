# create a empty dictionary
# add key an value..if key is exist retur as "key is exist"
# else add key and value

# global variable
details = {}
def addDictionary(key,value):
    if key in details:
        print( "key is exist ",key)
    else:
        print( "key is not  exist so adding the ",key)
        details[key] = value

addDictionary("name","test")
addDictionary("mobile","787979")
addDictionary("name","787979")