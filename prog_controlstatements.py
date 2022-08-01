'''

    condition
        5>3, 
        3==3, 
        2 is int, 
    
    if (condition):
        do if statement
    else:
        do else statement


'''


# a= 3
# b = 4


# if (a<b):
#     print ("YES")
# else:
#     print ("NO")

input_number = 2

# divisible by 2
if (input_number%2 == 0):
    
    print ("GIVEN NUMBER",input_number,"DIVISIBLE BY TWO")

    # print (f"GIVEN NUMBER {input_number} DIVISIBLE BY TWO")
# divisible by 3
elif (input_number%3 == 0):
    print (f"GIVEN NUMBER {input_number} DIVISIBLE BY THREE")
# divisible by 4
elif (input_number%4 == 0):
    print (f"GIVEN NUMBER {input_number} DIVISIBLE BY FOUR")
else:
     print (f"GIVEN NUMBER {input_number} NOT DIVISIBLE TWO,THREE,FOUR")