

'''
    # data types

    Integer
    Float
    String
    
'''

'''
    Example variable declaration

         5, 5.02, 'swathi' / "swathi" / """swathi"""
'''



a = 'rajeev'

# print (a)

# int a = 10
# a[][][][] <- 10
# int b = 10
# b[][][][]10 

# python storage process
#     [10]        <- a <- b
#(4306772520)


def addition(a,b):
    if (type(a) == int and type(b) == int):
        return (a+b)
    return None

sut = addition(4,'abd')   # test case 1 
print (sut)
# assert sut is None
sut = addition(4,5)
assert type(sut) is int   # test case 2
