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

# find and index are same in functionality except index gives fatal error
idxKing= msg.index('king')
print(f'"king" found at index {idxKing}')

idxQueen =msg.index('queen')
print(f'"queen" found at index {idxQueen}')

