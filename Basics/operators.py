''' 
Python has different operator
1. Mathematical
2. Condition
3. Assignment
4. Logical
5. Membership
6. Instance❌
7. Walrus'''

# Mathematical operator

a= 10*3
print(a)

a= 10/3  # division - real number
print(a)

a= 10//3 # integer division - quotient
print(a)

a= 10%3  # modulus
print(a)

a= 10**3  # exponent
print(a)

a= 10+3
print(a)

a= 10-3
print(a)

# Comparision

a=10
b=3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

# Assignment operator

c=15
print(c)
c+=15 # add 15 to existing value of c
print(c)
c-=15 # sub 15 to existing value of c
print(c)
c*=15 # add 15 to existing value of c
print(c)
c/=15 # add 15 to existing value of c
print(c)
c//=15 # add 15 to existing value of c
print(c)
c%=15 # add 15 to existing value of c
print(c)
c**=15 # add 15 to existing value of c
print(c)

# logical operator - multiple expression
a=5
b=10
c=15
print(a>b and a>c)
print(b>a or b>100)
print(not a>b)
print(a>b and a<c or a>10 )
print(not(a>b and a<c or a>10) )

# membership operator - in [it can search a value in a iterable]

colors = ['red','blue','green','purple','yellow']

print('red' in colors)
print('brown' in colors)
print(not('orange' in colors))

