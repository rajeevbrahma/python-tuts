


result_list = []
number_of_dictionaries_in_list = 4 
each_dict_count = 0

while (each_dict_count<number_of_dictionaries_in_list):

    while_loop_start_index = each_dict_count * 100 + 1

    while_loop_stop_index = 100 + while_loop_start_index

    dict_key_name = 1
    number_dict = {}
    
    while(while_loop_start_index<while_loop_stop_index):
        
        if (while_loop_start_index%2 == 0):
            number_dict.update({dict_key_name:while_loop_start_index})

            dict_key_name+=1

        while_loop_start_index+=1

    result_list.append(number_dict)
    
    each_dict_count+=1

print(result_list)


