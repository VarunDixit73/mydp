# WAP to ask the user his/her expences on different items. Take arround 15 key and value from user and then perform sum and avg on the values.

expences = {}
for i in range(15):
    k = input('enter a word->>')
    v = int(input('enter the meaning->>'))
    expences[k]= v

sum = 0
count = 0
for item in expences:
    sum = sum + expences.get(item)
    count+=1
avg = sum/count

print(expences)
print(sum)
print(avg)

'''
expences = {}
for i in range(15):
    k = input('enter a word->>')
    v = int(input('enter the meaning->>'))
    expences[k]= v

total = sum(list(expences.values()))
average = sum(list(expences.values())/len(expences))
print(f'total is {total}, average is {average}')
'''


