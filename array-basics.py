# store multiple values in same variable
# starts from 0,1....
a = [1,2,5,8,456]
b = [1,2,3,4]
# accessign value by index
print(a[0])
# to see all the values from array
for val in a:
    print(val)
print("total elements ",len(a))

# adding elements to the array in the last position
a.append(10)
a.extend(b)#merging two array into one
print("total elements ",len(a))

# adding the element in the position.if value is not exist.it will throw the error
a.insert(1,1202)
print(a)
# how many occurs in the array
times  =a.count(2)
print("count times ",times)

# to  get the position of the vlaue
print("index",a.index(1003))


try:
    print(a[10])#will throw the error
except Exception as e :
    print(e)