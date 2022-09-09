

"""

    Defining a function

    def <functionname>():
        '
        
        function block here
        
        
        '
    Calling a function

    functionname()


"""


from operator import add


def function_without_arguments(): # function definition
  a = 5
  b = 6
  # print (a+b)

function_without_arguments() # function call


def function_with_arguments(a,b):
  print (a)
  print (b)
  print (a+b)

a=6
b=9
function_with_arguments(a,b)

def print_name(first_name="no",last_name="No name"):
  print (f"First name is {first_name} and Last name is {last_name}")

# first = "R"
# last = "T"

print_name("R")


# write a function to append an element to a list


def add_element(element):
  list_variable = []
  list_variable.append(element)
  print (list_variable)

add_element(4)


def mulitply():
  return (4*3)


result = mulitply(5,4)
print (result)
print (mulitply(6,7))

def calculator():
  print (mulitply(8,4))

calculator()









def add(a,b):
  print (a+b)

add(5,4)
add(6,5)
add(8,9)


























def function_with_out_arguments():
  a = 5
  b = 6
  print (a+b)

def function_with_arguments(a,b):
  print (a+b)

def function_with_default_arguments(b,a=5):
  print (a+b)

def function_with_arguments_and_return(a,b):
  return (a,b)

r = function_with_arguments_and_return(4,5)
print (r)



# recursion

def recursion_with_arguments_and_return(a):
  a-=1
  print (a)
  if (a>0):
    recursion_with_arguments_and_return(a)

recursion_with_arguments_and_return(10)