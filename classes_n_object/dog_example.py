class Dog:

    def __init__(self,breed,weight,gender,color,age):
        self.breed = breed
        self.weight = weight
        self.gender = gender
        self.color = color
        self.age= age

# object

d1 = Dog('German Shepard',35,'M','White',2)
d2 = Dog('Boxer',10,'F','Grey',5)
d3 = Dog('Labrador',40,'M','Black',1)
d4 = Dog('Pug',15,'M','Brown',5.5)
d5 = Dog('Golden Retriever',45,'M','Golden',12)

print(d1.breed, d2.breed, d3.breed, d4.breed, d5.breed)
