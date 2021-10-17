class_9 = {
    'teacher' : 'PK Shukla Sir',
    'students':{
        '001' :{
            'name': 'Raja Babu',
            'father': 'Babu Ji',
            'grade': 'C'
        },
        '002' :{
            'name': 'Rajkumar',
            'father': 'Maharaj',
            'mother': 'Maharani',
            'grade': 'B'
        },
        '007' :{
            'name': 'James Bond',
            'father': 'J',
            'mother': 'O',
            'grade': 'A'
        },
    }
}

print(class_9)

from pprint import pprint

pprint(class_9)

# how to access data
print(class_9['students']['002']['father'])
print(class_9['students']['001']['grade'])
print(class_9['students']['007']['name'])

# loop

for k,val in class_9.items():
    print(k)
    if isinstance(val,str):
        print(val)
    if isinstance(val,dict):
        for k,data in val.items():
            print(k, end=' ->')
            if isinstance(data,str):
                print(data)
            if isinstance(data,dict):
                for k,v in data.items():
                    print(k, end=' ->')
                    if isinstance(v,str):
                        print(v)

