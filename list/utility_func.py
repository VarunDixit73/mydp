x=[1,2,3,12,3,2,1,3,1,2,123,222,432]
print(x)

print(x.count)

print(x.count(1), "occurence of 1")
print(x.count(2), "occurence of 2")
print(x.count(3), "occurence of 3")
print(x.count(123), "occurence of 123")
print(x.count(5), "occurence of 5")

# sort

a= ['Chicago','New York','Dallas']
b= [12,45,13]
c= ['Nevada',57,'Massouri',58]

print(a)
a.sort()
print(a)

print(b)
b.sort()
print(b)

print(b)
b.sort(reverse=True)
print(b)
'''
ERROR
print(c)
c.sort()
print(c)'''

y=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
print(y)
y.reverse()
print(y)

idx= y.index(3)
print(idx)

if 123 in y:
    idx = y.index(123)
    print('123 found at',idx)

z= x.copy()
print(z)
print(x)
x.sort
print(x)
print(z)
