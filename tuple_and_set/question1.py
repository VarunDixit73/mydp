# wap to add values from user in aset
# the user can add any no. of values in the set
# use while loop to perform this task

'''x = set()
val = int(input('Enter a value for set:'))
while val > 0:
    value = input('->')
    x.add(value)
    val-=1
print(x)'''

y = set()
while True:
    x = input('Enter a value:->>')
    if not x:
        break
    y.add(x)

print(y)