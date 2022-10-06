


class HouseEvaluation:

    landRate = 200           # class variable
    

    def __init__(self,engineer,seller,buyer,address):
        self.engineer = engineer
        self.seller = seller
        self.buyer = buyer
        self.address = address
        self.evaluation_score = 0
        self.__seller_price = 0     # protected variable
        self._private_variable = 0  # private variable
        

    def __proofOfOwnerShip(self):         # protected method
        return True        
        
    def setSellerPrice(self,price):
        self.__seller_price = price

    def sqft(self,length,breadth):
        self.sqft = length*breadth

    def engineersRemarks(self,score):
        self.evaluation_score = score

    def verifiedSeller(self):
        return self.__proofOfOwnerShip()
    

    def price (self):
        calculated_price = self.sqft * HouseEvaluation.landRate * self.evaluation_score
        if (self.__seller_price < calculated_price):
            return calculated_price
        elif(self.__seller_price > calculated_price):
            return self.__seller_price
        else:
            return None 




h1 = HouseEvaluation("Paul","Mark","Sriharsha","4,city")

h1.sqft(30,40)
h1.setSellerPrice(100000)

h1.engineersRemarks(0.8)
print (h1.verifiedSeller())

# print (h1.__proofOfOwnerShip())   # cant access this protected method
# print (h1.__seller_price)         # cant access this proetected variable

print ("H1 PRICE - ",h1.price())




h2 = HouseEvaluation("Ben","Mark","Joseph","4,city")

h2.sqft(4,9)
h2.engineersRemarks(0.3)        # engineer score
print (h2.verifiedSeller())     # Seller verification result
print ("H2 PRICE - ",h2.price())              # Final price for house 2

