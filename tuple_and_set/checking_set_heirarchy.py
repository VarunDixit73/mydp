x = {1,2,3,4,5,6,7,8,9,0}
y = {2,4,1,5}
z = {11,12,13,14}
a = {1,2,3,99,60}

print('x is superset of y', x.issuperset(y))
print('x is superset of z', x.issuperset(z))
print('x is superset of a', x.issuperset(a))

print('y is superset of x', y.issuperset(x))
print('y is superset of z', y.issuperset(z))
print('y is superset of a', y.issuperset(a))

print('a is unrelated of x', x.isdisjoint(x))
print('a is unrelated of y', x.isdisjoint(y))
print('a is unrelated of z', x.isdisjoint(z))
