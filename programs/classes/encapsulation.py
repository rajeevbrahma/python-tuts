"""

    Data hiding
    Read only


"""




class Book:
    """class space"""
    publisher = "P1"
    
    def __init__(self,author,book_name):
        # print (f"{author},{book_name}")
        self.author = author
        self.book_name = book_name
        self.__priceFormula = 100  # based on the author popularity and paper quality
        # self._price = self.__priceFormula

    def edit_formula(self,x):
        self.__priceFormula = x
        return self.__priceFormula

    def display(self):
        return (f"{Book.publisher}'s Book name is {self.book_name} and the author is {self.author}")

b1 = Book("1","2")

print (b1.display())
print (b1._price)
# print (b1.__priceFormula)
print (b1.edit_formula(2))
print (b1._price)