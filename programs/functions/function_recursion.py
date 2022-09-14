
# """

#     10 

#     WRITE A FUNCTION WHICH TAKES AN INTEGER AS AN ARGUMENT 
#     AND DECREASE ONE STEP AT A TIME AND PRINT THE RESULT

#     10
#     9
#     8
#     7
#     6
#     5
#     4
#     3
#     2
#     1



# """

# def negative_step_func(a):

#     for i in range(a):
#         print (a)
#         a-=1
        



# def negative_step_func(a):
#     for i in range(a,0,-1):
#         print (i)
 
# # negative_step_func(5)




# def negative_step_recurv_func(a):
#     a-=1
#     print (a)
#     if (a>0):
#         negative_step_recurv_func(a) # recursive function call based on condition

# # negative_step_recurv_func(10) # normal function call

# # factorial of a number using recursion


result = 1

# # 7*6*5*4*2*1


def factorial_of_a_number_using_recursion(result,a):
    
    result*=a
    a-=1
    print (result)    
    if (a>0):
        factorial_of_a_number_using_recursion(result,a) #recursive function call    
    


# factorial_of_a_number_using_recursion(result,7) # function call 



# def recur_func(a):
#     if a == 1:
#         return a
#     return a*recur_func(a-1)

# print (recur_func(7))




# Write a program to add a number to itself till it reaches a maximum value

maximum_value = 60
start_number = 1

def add_number(number):   # 1

    number+=number      # business logic -> 2
    
    if (number < maximum_value):   # True
        print (number)             # 40
        add_number(number)         # recursion function call with 40
        

print ("hello")
        
# add_number(start_number)            # normal function call


# write a program to add squares of a number to list till it reaches maximum value

#[1,4,9,16,25.....100]

start_number = 1
maximum_value = 10
list_variable = []

def squaring_numbers(number):    # 1
    
    square_of_a_number = pow(number,2)  # squaring a number 1
    
    list_variable.append(square_of_a_number)  # adding the result to the list [1]
    
    if (number < maximum_value):    # checking for the recusion condition True
        print (number)          # 1
        number = number + 1
        squaring_numbers(number) # recursion function call
        
squaring_numbers(start_number)  # function call

print (list_variable)




"""
    [room 1 [room 2 [room 3] ] ]


    enter a room 1
            switch off tv 1
            
            entering room 2
                switch off tv 2
                
                entering room 3
                    swtich off tv 3
                    switch off ac 3
                
                switch off ac 2 
            
            switch off ac 1






"""












# def add_number(number):

#     if (number > maximum_value):
#         return number
    
#     return add_number(number+number)
    

# print (add_number(start_number))




