
"""

    Poly Morphism

    Same method name with different behaviour

"""



class Bird:
    def about(self):
        print ("Birds are of various kinds ")
    def canFly(self):
        print ("Some can fly and some cant")

class Parrot(Bird):
    
    def canFly(self):
        print ("Can Fly")

class Hen(Bird):

    def canFly(self):
        print ("Cannot Fly")
    
p = Parrot()
p.canFly()


h = Hen()
h.canFly()


