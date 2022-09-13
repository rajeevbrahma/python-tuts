
"""

    10 

    WRITE A FUNCTION WHICH TAKES AN INTEGER AS AN ARGUMENT 
    AND DECREASE ONE STEP AT A TIME AND PRINT THE RESULT

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1



"""

def negative_step_func(a):

    for i in range(a):
        print (a)
        a-=1
        



def negative_step_func(a):
    for i in range(a,0,-1):
        print (i)
 
# negative_step_func(5)




def negative_step_recurv_func(a):
    a-=1
    print (a)
    if (a>0):
        negative_step_recurv_func(a) # recursive function call based on condition

# negative_step_recurv_func(10) # normal function call

# factorial of a number using recursion


result = 1

# 7*6*5*4*2*1


def factorial_of_a_number_using_recursion(result,a):
    
    result*=a
    a-=1
    print (result)    
    if (a>0):
        factorial_of_a_number_using_recursion(result,a) #recursive function call    
    

    

factorial_of_a_number_using_recursion(result,7) # function call 



# def recur_func(a):
#     if a == 1:
#         return a
#     return a*recur_func(a-1)

# print (recur_func(7))
