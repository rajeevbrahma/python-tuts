"""
    Tuples are ordered
    To store multiple values of various datatypes
    Can access using the index
    "immutable / unchangeable"

    (1, 2, 3)
     0, 1, 2
    -3 -2 -1


    ( 1, 2, 3, True, ( 1, 2, 3 ), [ 1, 2, 3 ],{ 1:1, 2:2 }, 6.7 )
                       0  1  2      0  1  2      
      0  1  2   3         4            5            6        7




"""


# how to define a tuple
tuple_variable_1 = ('John','Mark','Joseph','John')

tuple_variable_2 = ('JOHN',)

tuple_variable_3 = 'john','Luke',1,2,True

not_tuple_variable = ('JOHN')

# how to access tuples

print (tuple_variable_1[0])  # positive index
print (tuple_variable_1[-1]) # negative index
print (tuple_variable_1[:2]) # slicing

# how to update tuple values

tuple_variable_1 = tuple(list(tuple_variable_1).append("New Name"))


# Tuple methods
print (tuple_variable_1.count())
print(tuple_variable_2.index('John'))


a = (1,2,3,4,5)

list_of_tuples_variable = [(1,2),(3,4),(5,6)]

# iterating through list of tuples
for tuple_value in list_of_tuples_variable:
    print (tuple_value)
    for value in tuple_value:
        print (value)

for x,y in list_of_tuples_variable:
    print (x)
    print (y)

# iterating through list of lists

list_of_lists_variable = [[1,2,3],[3,4,5],[5,6,7]]

for x,y,z in list_of_lists_variable:
    print (x)
    print (y)
    print (z)

# iterating through dictionary
dict_variable = {1:"a",3:"b",5:"c"}

for key in dict_variable:
    print (key)


print (dict_variable.items())
# iterating through list of tuples which has key and value from a dictionary
for key,value in dict_variable.items():
    print (key)
    print (value)


