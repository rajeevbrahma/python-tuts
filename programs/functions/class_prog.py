
from unicodedata import name


def add(a,b):
    return (a+b)
    # print (a+b)

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


 #  y = (9)-3  - equation 1 
 # y = (42/7)-3+6
 # y = (4*3*2)+(4/2)-1

def equations():
    a = 5
    b = 4
    c = 3
    result = add(a,b)
    print ("line 22",result)
    print (add(a,b),c)
    print (sub(add(a,b),c))

    # y = (42/7)-3+6

    print (add(sub(div(42,7),3),6))

    print (sub(add(mul(mul(4,3),2),div(4,2)),1))


    # sub(result,c)


equations()



# write a function to get two operand inputs from the user and perform add/sub/mul/div 
# based on his choice (choice input)


operand_1 = int(input("Operand 1 here ")) # Assuming this is always a number
operand_2 = int(input("Operand 2 here ")) # Assuming this is always a number
function_choice = input("Select any one from the below \n1. add \n2. sub \n3. mul \n4. div\t")

if (function_choice == "1"):
    result = add(operand_1,operand_2)
    print (result)
elif(function_choice == "2"):
    result = sub(operand_1,operand_2)
    print (result)
elif(function_choice == "3"):
    result = mul(operand_1,operand_2)
    print (result)
elif(function_choice == "4"):
    result = div(operand_1,operand_2)
    print (result)
else:
    print ("You have entered an invalid choice")


# Can you 


"""
    bank_info = {
                    1234:{
                        name: Mark
                        balance : 34
                        pin:45
                    }
                    4567:{
                        name
                        balance
                        pin
                    }
                }





        Python Learnings Bank
    
    Please enter account number - 8943  # This account number should be 4 digit

    Please enter valid account number

    Account doesnt exists!! please try again

    Please enter your pin - 45 # pin number should always be 2 digit


        Welcom Mr Mark / Ms Leena
        

        please select from following options
            1. withdrawl
            2. balance display

            if 2 -> Your account has 34$

           if 1->  please enter amount you want to withdraw - 35

            if withdrawl amount is in the range please update the balance in the dictionary 
            else display insufficient funds message

        you want to continue 1 or 2 
        to exit press 3


"""

