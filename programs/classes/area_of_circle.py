class Formulas:

    pi = 3.14           # class variable
    
    def __init__(self,author):
        # self.result = 0  # instance variable
        self.author = author
        pass

    def areaOfCircle(self,radius):
        return  Formulas.pi * pow(radius,2)


c1 = Formulas("Paul")
print(c1.areaOfCircle(4))
print (c1.author)


c2 = Formulas("Jose")
print(c2.areaOfCircle(6))
print (c2.author)