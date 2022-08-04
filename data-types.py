"""
    write a program to print the following details of a person
1)
    Name,
    Age in years,
    hiehgt in centimeters
    weight in kilograms
    marital status
    height in feet
    no_of_kids
    description

Notes - String is actually itereable value means we can iterate through each and
and every character in a string, (we can actually access a string with its index)

"""


first_name = "John"                         # String
middle_name = ""                            # Empty String
last_name = "Kurup"

age = 25                                    # Integer
height_in_centimeters = 169     
Weight_in_kilograms = 80.78                 # Float
marital_status = False
height_in_feet = '5\'10' # or "5'10"        # escape sequence in string
no_of_kids = None                           # None type variable


                                            # example for multiline string
description = ' This is some descriptions \
about "Mr John" he is very \
asdfasdfads \
jsa;ldkjfasldjfa \
'


print (first_name)
print (age)
print (height_in_centimeters)
print (Weight_in_kilograms)
print (height_in_feet)
print (description)
print (no_of_kids)

# ------------------- TYPE OF VARIABLE --------------------

print (type(first_name))
print (type(age))
print (type(height_in_centimeters))
print (type(Weight_in_kilograms))
print (type(height_in_feet))
print (type(description))
print (type(no_of_kids))

# ---------------- ACCESS A STRING WITH ITS INDEX ---------------

"""
    John  -> String Value
    ||||
    0123  -> Character index value

    John Kurup  -> String Value
    ||||||||||
    0123456789  -> Character index value

    Note : Space is also considered as a character here.
    Note : The above indexing is positive indexing

    Related concepts :
            Negative indexing of a string
            String slicing

"""


print (first_name[0])           # index 0 Character in the string
print (first_name[1])           # index 1 Character in the string
print (first_name[2])           # index 2 Character in the string
print (first_name[3])           # index 3 Character in the string



