a = [10,1,3,2,5,8,456]
print(a)

#sorting the elements.it will change the position also
# a.sort()
# reverse sorting.
a.sort(reverse=True)
print(a)
print(a[0])#456
a.remove(456)#remove by value
a.pop(0)#remove by index
print(a)