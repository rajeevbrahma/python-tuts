
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