# wap to take user input to create a list
# the user should decide the size of list
# the list should be numeric
# display list values, sum, min, max, mean of the list

x_list=[]
size = int(input('Enter the size of the list:'))
for x in range (size) :
    val= int(input(f'{x+1}>>>>'))
    x_list.append(val)

total= sum(x_list)
min_list= min(x_list)
max_list= max(x_list)
mean = total/ len(x_list)

print(total)
print(min_list)
print(max_list)
print(mean)

