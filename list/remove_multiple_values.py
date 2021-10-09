x=[1,2,3,1,2,3,1,2,33,11,33,5,10,6,44,
1,6,4,4,9,68,4,9,8,1,6,89,4,9,8,6,4,1,
6,5,1,0,3,3,1,6,48,9,6,4,1,6,0,31,6,41,
6,1,2,3,1,5,4,84,8,4,96,65]
print(x)
y=x.copy()

# remove all the 3s i the list
print(x)
for i in range (x.count(3)):
    x.remove(3)
print('Removed all 3s:')
print(x)

# removing all 3s with pp n index

while 3 in y:
    idx= y.index(3)
    y.pop(idx)
print(y)