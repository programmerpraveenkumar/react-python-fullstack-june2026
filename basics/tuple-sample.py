# order,not changeable

v1 = ('dfghdg','adsfd',552)

#accessing the value
print(v1[0])
# 
print(v1)
# total elements in the tuple
print(len(v1))

for v in v1:
    print(v)

if 552 in v1:
    print('552 is exist')
# replace will throw the error
# v1[0]="sfsad"#replacement cannot be done