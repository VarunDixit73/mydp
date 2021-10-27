class Movie:

    def __init__(self,name,genre,year):
        self.name = name        # instance variable
        self.genre = genre      
        self.year = year

    def show(self):
        print('Details',self.name,"/".join(self.genre),self.year) 

m1 = Movie('Free Guy',['Comedy','Action'],2021)
m2 = Movie('Dune',['Sci-Fi','Action'],2021)

m1.show()
m2.show()