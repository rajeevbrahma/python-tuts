class Address:
    # def __init__(self,street,city):
    #     self.street = street
    #     self.city = city

    def addStreet(self,street):
        self.street = street

    def addCity (self,city):
        self.city = city


class Customer(Address):
    def __init__(self,name,age):
        # super().__init__()
        self.name = name
        self.age = age



c = Customer("12",1)
print (c.name)
# print (c.addCity(1))   # not yet defined
# print (c.city)



class Grandparents:
    def __init__(self,grandma,grandpa):
        self.grandma = grandma
        self.grandpa = grandpa
        self.netWorth = 100
        self.__familyLockerPassword = "1234"
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

    def addFamilyAssets(self,asset,type):
        self.familyAssets[type].append(asset)
    

class Parents(Grandparents):
    def __init__(self,mom,dad,grandma,grandpa):
        Grandparents.__init__(self,grandma,grandpa)
        self.mom = mom 
        self.dad = dad
    
    def addDigitalAssets(self,asset):
        if "digital" in self.familyAssets:
            self.familyAssets["digital"].append(asset)
        else:
            self.familyAssets["digital"] = [asset]



fam = Parents("Mom","Dad","GrandMa","GrandPa")
print (fam.mom)
print (fam.netWorth)
fam.addMoney(1000)
print (fam.netWorth)