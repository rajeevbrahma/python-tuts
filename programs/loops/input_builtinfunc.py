
from re import M
from tkinter import N


details = {}
first_name = input("Please Enter a First Name")
last_name = input("Please Enter a Last Name")


# 1 and 0     0
# 0 and 1     0
# 1 and 1     1
# 0 and 0     0



            # N         M
            # False or True  True         False
            # M         N
            # True  or False True         False
            # N         N
            # False  or False False       False
            # M        M
            # True      True   True        True

while(first_name != "N" and last_name != "N"):
    details.update({"first_name":first_name})
    details.update({"last_name":last_name})
    first_name = input("Please Enter a First Name")
    last_name = input("Please Enter a Last Name")
    

print (details)

# name with less than 5 characters is not allowed to add in the dictionary

