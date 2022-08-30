
# solution 1

even_numbers = []

for outer_range in range(0,4):
    
    even_numbers_dict = {}
    even_numbers.append(even_numbers_dict)
    
    dict_key_name = 1

    if (outer_range < 1):
        start_index = 1
    else:
        start_index = outer_range*100 + 1
    
    for inner_range in range(start_index,100+start_index):
        
        if (inner_range%2 != 0):
            continue
        
        even_numbers_dict.update({dict_key_name:inner_range})
        
        dict_key_name+=1

    even_numbers[outer_range] = even_numbers_dict

print (even_numbers)



"""
    [
        {1:2,2:4....},
        {1:102,2:204....},
        {}

    ]

"""

# solution 2 
result_list = []
number_of_dictionaries_in_list = 4 


number_dict = {}    

for each_dict_count in range(number_of_dictionaries_in_list):

    for_loop_start_index = each_dict_count * 100 + 1   # 201

    for_loop_stop_index = 100 + for_loop_start_index  # 301


    dict_key_name = 1

    for each_number in range(for_loop_start_index,for_loop_stop_index):
                                        
        if (each_number%2 == 0):            
            number_dict.update({dict_key_name:each_number}) 
        
            dict_key_name+=1

    result_list.append(number_dict)


print (result_list)                 # {1:4}











