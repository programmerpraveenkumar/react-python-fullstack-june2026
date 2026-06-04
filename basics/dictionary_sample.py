# key and value
# key should not duplicate.value can be duplicate
dictionary1={
    "name":"ashok",
    "age":"2",
    "age":"4",
    "country":"some country"
}
# adding new value
dictionary1['mobile'] = 656565656
print(dictionary1)
# update the value
dictionary1['age']=6
print(dictionary1)
# accessing the value by the key
print(dictionary1['name'])

print("----")
for key in dictionary1.keys():
    print(key)
print("----")
for v in dictionary1.values():
    print(v)
print("----")
for k,v in dictionary1.items():
    print(k,v)   

# match operator
if "firstname" in dictionary1:
    print(dictionary1['firstname'])

#specified key will be removed
dictionary1.pop("country")
# last added value will be removed
dictionary1.popitem()
print(dictionary1)
