
class IceCream:

    def __init__(self,flavour,price,brand,style):
        self.flavour = flavour
        self.price = price
        self.brand = brand
        self.style = style

# object
ice1 = IceCream('Chocolate',30,'Amul','Bar')
ice2 = IceCream('Vanilla',25,'Quality Walls','Cone')

print(ice1.brand, ice1.flavour)
print(ice2.brand, ice2.flavour)

