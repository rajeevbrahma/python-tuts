
def function_with_variable_within_it():
    a = 500
    print (a)

function_with_variable_within_it()
print (a)



b = 300
def function_with_variable_within_it():
    b = 500
    print (b)

function_with_variable_within_it()
print (b)


def function_with_global_variable():
    global c
    c = 100
    print (c)

function_with_global_variable()
print (c)

