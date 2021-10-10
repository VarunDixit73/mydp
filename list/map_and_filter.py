x= [12,34,56,67,89,9]
words= "Python is the best language for coding".split()

'''
map() - modern way for mapping a sequence for a operation in 1 line
filter() - modern way for filtering a sequence using condition in 1 line
'''

'''
map() and reduce() are lazy objects concept, in which data is not consuming memory until it is called to a particular datatype like list, tuple, set 
'''

x2= list(map(lambda i: i**2,x))
y= [2,5,7,8,3,10]

xy= list(map(lambda i,j: i+j,x,y))
print(xy)

f= lambda i,j: i+j
xy= list(map(f,x,y))
print(xy)

# filtering

words_with_n= list(filter(lambda i:"n" in i, words ))
print(words_with_n)

