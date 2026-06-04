status = False;
if status:
    print('this is true')
else:
    print('this is false')

# always starts from 0
for i in range(13):
    if i%2 == 0:
        print("even")
    else:
        print(i)

print("------------")
# start from 10 to 15 increase by 1
for i in range(10, 15,2):
    print(i)

print("------------")
count = 4
while count < 3:
    print(count)
    count += 1