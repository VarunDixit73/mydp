a=10
b='balls'
c= 100
d= 'Rupees'

#printing with , seperated values
print("Raju purchased",a,b,'for',c,d)

#concatination using +
#print("Raju purchased" + a + b + 'for' + c + d)
#can't concatinate sting and integer together

print("Raju purchased" + str(a) + b + 'for' + str(c) + d)

#printing format specifier
print("Raju purchased %d %s for %d %s"%(a,b,c,d))

# print using format() method
print("Raju purchased {} {} for {} {} ".format(a,b,c,d))

# printing using f.string (from version 3.6)
print(f'Raju purchased {a} {b} for {c} {d}')

#properties of print function
# end - handles what will be displayed after printing content
# sep - seperator symbol

print('Hi',end=" ")
print('there')

print(a,b,c,d)
print(a,b,c,d, sep="✔")

