name = "Vijay Deenanath Chauhan"
print('size:',len(name))

print(name[2],name[3],name[4]) # noob implementation

print(name[2:5]) # pro implementation

print(name[6:-8])

# we can skip value before colon if we want to start from begining
# we can skip value after if we want to stop at the end

print(name[:5])         # first five char char from 0-4 index
print(name[-7:])        # last 7 char from -7 to end index

# syntax for slicing
# var[startIdx : endIdx : Gap]

print(name[::2]) # start to end with gap of 2 index
print(name[1::2])   # 1 index to end with gap of 2 index

# Reverse String
print(name[::-1])
print(name[:])
print(name[:][::-1][:5])
