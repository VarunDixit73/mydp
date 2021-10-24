# count no. of chars, words, punctuation, spaces from file

file = open('wiki.txt','w')
data =''
count = 0
counter = 0
while True:
    line = input(':->>>').casefold()
    if line:
        data+=line +'\n'
    else:
        break

for val in data:
    if val == ' ':
        count+= 1
        continue
    else:
        char_list = list(data)
        counter+= 1


file.write(data)
file.close()

list1 = list(data.split(' '))
count_l1= len(list1)
file.close()

print('Number of spaces is :->>>',count)
print('Number of characters is:->>>',counter)
print('Number of words is :->>>',count_l1)