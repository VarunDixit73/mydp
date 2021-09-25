msg= "We will be victorious"

for c in msg:
    print(c)

for c in enumerate(msg):
    print(c)

for i,c in enumerate(msg):
    print(i,c)

for i,c in enumerate(msg):
    if i%2!=0:
        print(c,end='')

for i,c in enumerate(msg):
    if i%2==0:
        print(c,end='\n')       