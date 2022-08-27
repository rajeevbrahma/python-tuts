even_numbers_dict = {}
index_variable = 1
even_numbers = []

a = 1
    
for i in range(1,300):
    if (i%2 != 0):
        continue
    
    # print (i,index_variable)
    even_numbers[0] = even_numbers_dict.update({index_variable:i})
    a +=1
    
print (even_numbers_dict)


# [ 
    # {1:2,2:4,3:6 ........ 49:98},
    # {1:102,2:104,3:106 ........ 49:198},
    # {1:202,2:204,3:206 ........ 49:298}
   
# ]