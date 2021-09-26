'''
break keyword is important in loops
as it helps us to allow stopping the loop before completion.
'''

name= input('What is your name: ')
size= len(name)
print(size)
while size> 0:
    size-= 1
    if name[size]== ' ':
        print('\nSpace found in name')
        break
    else:
        print(name[size],end='')

