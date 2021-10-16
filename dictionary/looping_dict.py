stdDict = {
    'name'      : 'Billu',
    'maths'     : 17,
    'english'   : 15,
    'hindi'     : 12,
    'age'       : 14,
    'studies'   : False,
    'deliquent' : True,
    'phone'     : 9393939393
}

# looping dict
print('only keys from dictonary in a for loop')
for item in stdDict:
    print(item,end=' ')

print('\nonly values from dictonary in a for loop')
for item in stdDict:
    print(stdDict[item],end=' ')

print('\nkeys and values from dictonary in a for loop')
for item in stdDict:
    print(item, stdDict[item],end=' ')

print('\nkeys and values from dictonary in a for loop')
for k,v in stdDict.items():
    print(k,'=>',v,end=' ')
