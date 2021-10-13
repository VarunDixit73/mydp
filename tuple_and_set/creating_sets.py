x = set() # empty set

x = {1,2,3,1,2,3,1,2,3,1,2,3,1,2,3}
y = list(x)
print(x)
print(y)

words = {'Knights','Radiants','Shards','Blades','Armor'}
print(words)

for value in words:
    print(value,end=' ')

quote = "Life Before Death, Courage Before Fear,Journey Before Destination"
quote_chars = set(quote.casefold())
print(quote_chars)

