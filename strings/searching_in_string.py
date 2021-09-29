msg= 'once upon a time, their was a kingdom. The king was Richard'

# find()- better
# index()

idx= msg.find('time')
print(f'"time" was found at index {idx}')

idx= msg.find('Queen')
print(f'"Queen" was found at index {idx}') # -1 means the entered value was not in the string
if idx==-1:
    print(f'"Queen" was not found.')

idxKing= msg.find('king')
print(f'"King" was found at index {idxKing}')

idxA= msg.find('a')
print(f'"King" was found at index {idxA}')
print(len(msg))