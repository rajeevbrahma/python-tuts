"""

    for, while

    You can loop through any iterables

        list
        dictionary
        string

    * usually membership operator keyword "in" will be used here along with for keyword

    example_list = [1,2,3,4]
    example_dict = {0:1,1:2,2:3}
    example_string = "Python"

    for

        syntax : 
                for char in example_string:
                    print (char)

                for list_element in example_list:
                    print (list_element)
                
                for dict_key in example_dict:
                    print (dict_key)

                for number in range(10):
                    print (number)


    while

        syntax :
                number = 10
                while (number<10)
                    print (number)
                    number += 1
                

"""

example_string = "Python"

# print (example_string)

temp_string = ""
for i in example_string[::-1]:
    temp_string +=i

print (temp_string)

# for i in example_string[::-1]:
#     print (i)


# for number in range(10,100,10):
#     print (number)

# for character_index in range(2,len(example_string)-2,2):
#     print (example_string[character_index])



