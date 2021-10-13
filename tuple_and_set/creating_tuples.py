a = (1,2,3)
b = 12,34,36

print(a,b)
print(type(a),type(b))

c= ('Chimera','Minotaur','Persues')
print(c[0])     # accessing value from index
print(c[1])
print(c[-1])

# creating tuple from existing data
name = 'Rahul'
nameT = tuple(name)
print(nameT)

values = [1299,239,8329,1239]
values = tuple(values)  # original variable converted to tuple < UPDATE

a = 10
b = 12

x = a,b
print(x)


