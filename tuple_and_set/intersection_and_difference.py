x = {1,2,3,4,5,6,11,23}
y = {1,2,3,5,6}

common = x.intersection(y)
print('x and y have',common)

xuniq = x.difference(y)
print('x has unique values',xuniq)


yuniq = y.difference(x)
print('y has unique values',yuniq)

# not to be used in code actually
x.intersection_update(y)
print(x)

y.difference_update(x)
print(y)

