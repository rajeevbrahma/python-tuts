
# def function_with_variable_within_it():
#     a = 500
#     print (a)

# function_with_variable_within_it()
# print (a)



# b = 300
# def function_with_variable_within_it():
#     b = 500
#     print (b)

# function_with_variable_within_it()
# print (b)


# def function_with_global_variable():
#     global c
#     c = 100
#     print (c)

# function_with_global_variable()
# print (c)


# globla space

a = 100 # global variable


def func():
    # local space
    # a = 500 # local variable
    print ("Inside func",a)
    print (b)

def func_with_global_variable():
    # global b  # We want this locally created variable to be treated as a global variable
    global b
    b = 400



func_with_global_variable()   
func()

print (a)
print (b)

