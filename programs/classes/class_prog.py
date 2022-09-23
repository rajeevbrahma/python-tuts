"""
    understand the class 

    class variable, instance variable

    constructors

    method ? 

    oops principles

            encapsulation
            inheritance
            abstraction
            polymorphism


"""







a = 10
b = "python"
c = True

print (type(a))
print (type(b))

class Calculator:

    # default method-  this method is going to be called on object creation
    # init constructor which accepts some arguments
    def __init__(self,op1,op2):
        self.op1 = op1
        self.op2 = op2

calc_1 = Calculator(1,2)
calc_2 = Calculator(1,2)

print (calc_1,type(calc_1))
print (calc_2,type(calc_2))


calc_1.operand_1 = 3     # instance variable
calc_2.operand_2 = 4


# print (calc_1.operand_2)


class Calculator:

    """CLAS SPACE"""
    result = 100   # Class variable

    # default method-  this method is going to be called on object creation
    # init constructor which accepts some arguments
    
    def __init__(self,op1,op2):
        print ("Instantiation started")
        """METHOD SPACE"""
        # Calculator.result = 0   # Class variable
        
        self.op1 = op1          # instance variable
        self.op2 = op2          # instance variable


# Calculator.result = 10

print ("OBJ 1")
calc_1 = Calculator(1,2)
print (calc_1.op1)
print (calc_1.op2)

calc_1.result = 9   # modifying the class variable from an instance
print (calc_1.result)      
print (Calculator.result)  

print ("\nOBJ 2")

calc_2 = Calculator(4,3)
print (calc_2.op1)
print (calc_2.op2)
print (Calculator.result)


class Transactions:

    dollar_rate = 10   # class variable

    def __init__(self,amount,payer,payee,name):
        self.amount = amount   # instance variable
        self.payer = payer     # instance variable
        self.payee = payee     # instance variable
        bank_name = name       # method variable
        print (f"Welcome to {bank_name} Bank")       

    def conversion(self):
        return self.amount * Transactions.dollar_rate    


txn_1 = Transactions(5,"1","2","B1")

txn_2 = Transactions(6,"2","4","B2")

print (Transactions.dollar_rate)



print (txn_1.conversion())
print (txn_2.conversion())



class Book:
    """class space"""
    publisher = "P1"
    
    def __init__(self,author,book_name):
        # print (f"{author},{book_name}")
        self.author = author
        self.book_name = book_name
        self.__price = 10

    def edit_private(self,x):
        self.__price = x
        return self.__price

    def display(self):
        return (f"{Book.publisher}'s Book name is {self.book_name} and the author is {self.author}")



"Book name is ..... and the author is ....."

"P1"

b1 = Book("autho 1","book 1")
b2 = Book("autho 1","book 2")
b3 = Book("autho 2","book 3")

print (b3.edit_private(4))


# b3._price = 1
# print (b3.price)

# print (b1.display())
# print (b2.display())
# print (b3.display())
