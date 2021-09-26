'''
we have continue keyword which is used to skip a loop step
it can be used in both for and while loop
'''

i= int(input('Enter value of i: '))
while i>0:
    if i%3==0:
        i-=1
        continue
    print(i)
    i-=1

# we can easily skip the continue keyword
j= int(input('Enter value of j: '))
while j>0:
    if j%3==0:
        j-=1
    print(j)
    j-=1
