value= input("Enter something: ")

ans= value.isupper()
print("Is the value entered is Upper? ",ans)

ans= value.islower()
print("Is the value entered is Lower? ",ans)

ans= value.isalpha()
print("Is the value entered contains only alphabet? ",ans)

ans= value.isnumeric()
print("Is the value entered contains only numerals? ",ans)

ans= value.isspace()
print("Is the value entered contains only space? ",ans)

ans= value.isprintable()
print("Is the value printable? ",ans)

ans= value.isdigit()
print("Is the value entered contains only digits? ",ans)

ans= value.isdecimal()
print("Is the value entered contains only decimals? ",ans)

name= "Dr. Ram Verma"
if name.startswith('Dr'):
    print('Hello Doc!')
if name.startswith('Mr'):
    print('Hello Mister')

file= input('Enter the filename:')
if file.endswith('.doc'):
    print(f'{file} is word file')
elif file.endswith('.pdf'):
    print(f'{file} is PDF file')
elif file.endswith('.png'):
    print(file,'is Image file')