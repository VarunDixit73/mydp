# we have to make a class for storing information about cake

class cake:
    brand = 'JJ Bakery'
    flavour = 'Chocolate'
    weight = 1
    is_eggless = False
    color = 'brown'

cake1= cake()       # object 1
sasta_cake = cake() # object 2

sasta_cake.flavour = 'Strawberry'
sasta_cake.brand = 'Chandu Bakery'
sasta_cake.color = 'Pink'
sasta_cake.is_eggless = True
sasta_cake.weight = .25

print(cake1.flavour)
print(sasta_cake.flavour)

# redundant code
# length lines
# solution -> intro to constructor