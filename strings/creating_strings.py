name = 'Alex Mason'
city = 'New York'

story= '''this is a story about
alex mason, okay!
This guy is so good
that i can't tell you.'''

poem= """"
johnny johnny, yes papa
eating sugar, no papa
that's okay you did not lie
"""

print(type(name),type(city),type(story),type(poem))

print(name)
print(city)
print(story)
print()             # line change
print(poem)

properties='''
1.- Indexed
2.- Immutable
3.- str() is the constructor for creating the strings [type cast]
4.- It can be concatenated using +
5.- It can be duplicated using*
'''

print(properties)

name[0] = 'B' # will not work as strings are immutable
