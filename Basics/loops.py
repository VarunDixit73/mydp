'''
Syntax:
for temp_var in iterable:
    Statement 1
    Statement 2



    Statement N

Iterables can be of:
String
list
tuple
set 
dict
special functions like rangw(),zip(),enumerate()
anything with multiple elements
'''

num=[1,2,3,4,5,6,7,19,12]
for i in num:
    print(i)

msg= "We are now using loops"
print("Characters in msg:",len(msg))


# traversal
for char in msg:
    print(char)

for char in msg:
    if char!=" ":
        print(char)

# numeric loop

for i in range(10):
    print(i, end=',')
