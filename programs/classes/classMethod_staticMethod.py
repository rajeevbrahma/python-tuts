

class CustomerOps():
    
    customer_information = {}
    las_cust_num = 1

    def __init__(self):
        pass

    def add(self,name):
        self.customer_information.update({self.las_cust_num:name})
        self.incrementCustomerNumber()

    @classmethod
    def incrementCustomerNumber(cls):
        cls.las_cust_num +=1



bank_1 = CustomerOps()
bank_1.add("name 1")
bank_1.add("name 2")
print (bank_1.customer_information)
print (CustomerOps.incrementCustomerNumber())
