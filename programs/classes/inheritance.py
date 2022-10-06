
# self -  will the default argument for methods in the class
# to associate that method to the class

# Example : 
# class A:
#     def F(self):
#         pass



class Parent:
    def __init__(self,a,b):         # 
        self.a = a
        self.b = b
   

# super - keyword / buitin function ?  
class Child(Parent):            # Inheriting from the class Parent    
    def __init__(self,a,b,d):
        
        super().__init__(a,b)    # initialize the parent class variables
        self.d = d


c = Child("Mark","Mary","Tony")   #,"Tony"
print (c.a)
print (c.b)
print (c.d)


class P1:

    def displayP1(self):
        print ("We are P1")

class P2:
    def displayP2(self):
        print ("We are P2")

class C1(P1,P2):
    def displayC1(self):
        print ("I am C1")


c1 = C1()
c1.displayC1()
c1.displayP1()
c1.displayP2()



class H2:
    def __init__(self):
        print ("I am Hydrogen")
        self.forTrees = True

class O:
    def __init__(self):
        print ("I am Oxygen")
        self.fire = True
        self.usedForBreating = True
        

class H2O(H2,O):
    
    def __init__(self): 
        
        H2.__init__(self)
        
        O.__init__(self)
        
        print ("I am Water")
        print ("Can Drink")

h2o = H2O()
print (h2o.forTrees)
print (h2o.usedForBreating)
print (h2o.fire)









# # Method overriding example
# class Parent:
#     def func1(self):
#         print ('This is class 1')

# class Child(Parent):
#     def func1(self):
#         print ('This is class 2')

# c = Child()
# print (c.func1())



# # single inheritance, using super method example
# class Address:
#     def __init__(self,street,city):
#         self.street = street
#         self.city = city



# class Customer(Address):
#     def __init__(self,name,age,street,city):
#         super().__init__(street,city)
#         self.name = name
#         self.age = age


# c = Customer("12",1,"c","d")
# print (c.name,c.age,c.street,c.city)



# class Indian:
#     def __init__(self):
#         self.speaks = "Telugu"
         

# class American:
#     def __init__(self):
#         self.speak = "English"

# class IndoAmerican(American,Indian):
#     def __init__(self):
#         Indian.__init__(self)
#         American.__init__(self)
#         pass

# ia = IndoAmerican()
# print (ia.speaks)
# print (ia.speak)




class Grandparents:
    def __init__(self,grandma,grandpa):
        self.grandma = grandma
        self.grandpa = grandpa
        self.netWorth = 100
        self.__familyLockerPassword = "1234"  # private variable
        self.familyAssets = {
            "car":[
                "Hyundaii10"
            ],
            "house":[
                "7thstreet, Gen road, Maroon City"
            ]
        }
    def addMoney(self,money):
        self.netWorth+=money

    def takeMoney(self,howmuch,password):
        if (password == self.__familyLockerPassword and self.netWorth > howmuch):
            self.netWorth -= howmuch
            return True
        return False

    def addFamilyAssets(self,asset,type):
        self.familyAssets[type].append(asset)
    

class Parents(Grandparents):
    def __init__(self,mom,dad):
        # Grandparents.__init__(self,grandma,grandpa)
        self.mom = mom 
        self.dad = dad
    
    def addDigitalAssets(self,asset):
        if "digital" in self.familyAssets:
            self.familyAssets["digital"].append(asset)
        else:
            self.familyAssets["digital"] = [asset]

class Child(Parents):
    def __init__(self,name,mom,dad,grandma,grandpa):
        Grandparents.__init__(self,grandma,grandpa)
        Parents.__init__(self,mom,dad)
        self.name = name
    pass

# fam = Parents("Mom","Dad","GrandMa","GrandPa")
# print (fam.mom)
# print (fam.netWorth)
# fam.addMoney(1000)
# print (fam.netWorth)

print ("\n MULTILEVEL INHERITANCE EXAMPLE---")
c = Child("name","Mom","Dad","GrandMa","GrandPa")
print (c.netWorth)

print (c.takeMoney(5,'1234'))

print (c.netWorth)