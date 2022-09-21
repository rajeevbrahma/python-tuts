
"""
    what is class 
    what is object 
    inheritance 
    instantiation 
    what is class attribute and instance attribute 
    what is class method 

    oops principles

        encapsulation
        abstraction
        inheritance
        polymorphism


"""



# creation of class 
class Transactions:
    pass 

# creating object from the class 
txn = Transactions()
print (txn,type(txn))

txn.number = 1
txn.status = True
print (txn.number,type(txn.number))
print (txn.status,type(txn.status))

# creating another object class
txn_2 = Transactions()
print (txn_2,type(txn_2))



# creating class with parameters
class Transactions:

    transactions = []
    dollar_rate = 79.0

    def __init__(self,amount,payer,payee):
        self.amount = amount 
        self.payer = payer
        self.payee = payee
        Transactions.transactions.append(self)
    
    # def dollar_conversion(self):
    #     return Transactions.dollar_rate * self.amount
    
    def __repr__(self):
        return f"{self.amount},{self.payer},{self.payer}"

txn = Transactions("1",1,1)
txn2 = Transactions(1,2,2)
txn3 = Transactions(1,2,3)

print (txn.transactions[1])
print (txn.__dict__)            # list of all the instance level attributes
print (Transactions.__dict__)   # list of all the class level attributes

# for tn in txn2:
#     print (tn)



# class Address:

#     city = None
    
#     def __init__(self):
#         pass
    
#     def add_city(self,city):
#         self.city = city

# class CustomerOps(Address):
    
#     customer_information = {}
#     las_cust_num = 1

#     def __init__(self):
#         pass

#     def add(self,name):
#         self.customer_information.update({self.las_cust_num:name})
#         self.las_cust_num+=1
#         self.add_city()

#     def get(self,num):
#         print(self.customer_information[num])

#     def update(self,name):
#         self.customer_information.update({self.las_cust_num:name})
    
#     def remove(self,num):
#         del self.customer_information[num]

# bank_1 = CustomerOps()
# bank_1.add("name 1")
# bank_1.add("name 2")
# bank_1.add_city("city 1")
# print (bank_1.customer_information)


# class Calc:

#     model = "Calci"

#     def __init__(self,name):
#         self.name = name
#         Calc.model = "New one"
    

# a = Calc("hello")
# print (a.name)
# print (a.model)

# b = Calc("world")
# b.model = "Calc"
# print (b.name)
# print (b.model)
# print (a.model)

# c = Calc("hai")
# print (c.model)


# class MyClass:

#     def __init__(self):
#         self.name = "lao"
#     # def __enter__(self):
#     #     print ("Hello")

#     # def __exit__(self, exc_type, exc_val, exc_tb):
#     #     print ("World")

#     def __repr__(self):
#         return f"Hello {self.name}"



# print (MyClass())

# # with MyClass() as cls:
# #     print ("My class")



# # A simple Person class

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         rep = 'Person(' + self.name + ',' + str(self.age) + ')'
#         return rep


# # Let's make a Person object and print the results of repr()

# # person = Person("John", 20)
# # print(repr(person))