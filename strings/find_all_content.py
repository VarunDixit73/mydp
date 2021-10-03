'''
str find() function allows to pass starting index, and stop index for use.
'''

data= '''What are the codes for the safe. 
How safe is the safe. 
Is the safe really safe?
'''

start_idx = 0
for i in range(5):              # use str.count() for better output
    idx= data.find('safe',start_idx)
    print(f"'safe' word found at {idx}")
    start_idx=idx+1

print('while loop is better')
start_idx=0
while True:
    idx= data.find('safe',start_idx)
    if idx== -1:
        break
    print(f"'safe' word found at {idx}")
    start_idx=idx+1

