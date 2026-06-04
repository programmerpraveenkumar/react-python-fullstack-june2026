# its unique value.so it wont duplciate
#cannot access individual item
# inesrtion order wil not maintain
myset={
    "apple","orange","carrot"
}

myset1={
    "apple1","orange1","carrot1"
}
# myset[0]="grapes"#will throw the error
myset.add("new value")#to add the new values in the set
myset.add("orange")#it will not add.as its has this value already
print(myset)
# match operator `in`.to check the value exist or not
# print('aldfads' in myset)
if 'apple' in myset:
    print("it exist")
else:
    print("not exist")

# to loop all the values
for value in myset:
    print (value)

# joining the sets using union
# st_value = myset.union(myset1)
st_value = myset | myset1
print(st_value)
# set to list
list1 = list(myset)
print(type(list1))
print(type(myset))
print(list1)
print(list1[0])