class Shape:

    def __init__(self,w=0,h=0):
        self.width = w
        self.height = h
    
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2* self.width*self.height

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False

    def __repr__(self):
        return str(self.area())

items = [Shape(2,2),Shape(1,5), Shape(3,3),Shape(10,10),Shape(3,2)]
print(items)

if Shape(3,3) > Shape(3,2):
    print('yes')

items.sort()
print(items)