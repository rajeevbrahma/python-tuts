

details = {}

first_name = input("Please Enter a First Name :")
last_name = input("Please Enter a Last Name : ")


print (first_name)
print (type(first_name))
print (last_name)
print (type(last_name))



convert_to_int = "1"
convert_to_float = "2.4"
convert_to_str = 893
convert_to_list = "[1,2,3]"

print (type(convert_to_int))       
print (type(convert_to_float))
print (type(convert_to_str))
print (type(convert_to_list))

converted_to_int = int(convert_to_int)         # This should a number
converted_to_float = float(convert_to_float)   # This should a float value
converted_to_str = str(convert_to_str)         # 
converted_to_list = list(convert_to_list)

print ("\n")
print (type(converted_to_int))
print (type(converted_to_float))
print (type(converted_to_str))
print (type(converted_to_list))



# write a program to take two inputs from the user and add the result

def input_func():
    try:
        operand_1 = input(" Please give a number ")   # 1
        operand_2  = input (" Please give a number ") # 2
        
        converted_operand_1 = int(operand_1)
        converted_operand_2 = int(operand_2)
        
        result = int(converted_operand_1) + int(converted_operand_2)
        print (result)
    except Exception as e:
        print (e)
        input_func()

input_func()    





# updating a dictionary by taking inputs from the user
first_name = input("Enter first name")
last_name = input("Enter last name")

details = {"first_name":None,"last_name":None}

if (first_name != "" and last_name != ""):
    details.update({"first_name":first_name,"last_name":last_name})
else:
    print ("one of the strings is empty")
    
print (details)












while (first_name == "" and last_name == ""):
    details.update({"first_name":first_name,"last_name":last_name})
    print (details)
    first_name = input("Enter first name")
    last_name = input("Enter last name")
    


# make sure neither first or last name is empty string
# throw error when you see any of them empty
# update the dictionary with the first and last name






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

# while(first_name != "N" and last_name != "N"):
#     details.update({"first_name":first_name})
#     details.update({"last_name":last_name})
#     first_name = input("Please Enter a First Name")
#     last_name = input("Please Enter a Last Name")
    

# print (details)

# name with less than 5 characters is not allowed to add in the dictionary

# type casting 
# input 