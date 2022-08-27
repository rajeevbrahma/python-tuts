
even_numbers = []

for outer_range in range(0,4):
    
    even_numbers_dict = {}
    even_numbers.append(even_numbers_dict)
    
    dict_key_name = 1

    if (outer_range < 1):
        start_index = 1
    else:
        start_index = outer_range*100 - 1
    
    for inner_range in range(start_index,100+start_index):
        
        if (inner_range%2 != 0 or inner_range == 0):
            continue
        
        even_numbers_dict.update({dict_key_name:inner_range})
        
        dict_key_name+=1

    even_numbers[outer_range] = even_numbers_dict

print (even_numbers)
