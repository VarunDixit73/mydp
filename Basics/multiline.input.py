all_data= ''              # blank string

while True:               # infinite loop by default
    line = input("~")
    if not line:          # if line is not entered
        break             # stop loop
    all_data += line+'\n' # add the line to all data

print('Your Data:')
print(all_data)
print('you entered',len(all_data),end=' ')
