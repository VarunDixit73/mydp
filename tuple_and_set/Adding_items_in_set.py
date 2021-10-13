a = {1,2,3}

a.add(129)
a.add("Charbagh")
a.add((1,2,3))
print(a)
# error
#a.add([1,2,3])  # you cannot add alist, dict or set in a set
#print(a)

x = [1,2,3,4,456,565655,5544]
a.update(x)
print(a)

