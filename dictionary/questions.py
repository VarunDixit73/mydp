''' wap to create a dict that contains following sequence:
1:1
2:4
3:9
4:16
...
10: 10000
hint : use FOR loop, dont do this manually 
'''

dict1 = {}
for k in range(1,101):
    dict1[k]= k**2
print(dict1)

'''
wap to sort a dictionary of 5 elements. you can put anything inside the dictionary
'''

# sot by keys

colors = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'Y': 'yellow',
    'Bl': 'black'
}
print(dict(sorted(colors.items())))
