"""

    create an empty list.

    create a dictionary for the following keys



"""

from unicodedata import name


persons_details = [{},{}]   # list of empty dictionaries

# print ("DATATYPE of variable persons_details",type(persons_details))
# print ("DATATYPE of variable persons_details first elelment",type(persons_details[0]))

# first person details
persons_details[0] = {
                        "name":"Mark",
                        "age":25,
                        "married":False,
                        "pets":None,
                        "height":166.97

                    }

persons_details[1] = {
                        "name":"John",
                        "age":30,
                        "married":True,
                        "family_details":{
                            "wife_details":{
                                "name":"Mary",
                                    #   0123
                                "age":28
                            },
                            "children":[
                                            {
                                                "name":"Jr John",
                                                "age":3
                                            },
                                            {
                                                "name":"Jr Mary",
                                                "age":6
                                            }
                                        ]

                        },
                        "pets":3,
                        "height":155.34

}
print (persons_details[1]["family_details"]["wife_details"]["name"][-1])
print (persons_details[1]["family_details"]["children"][0]["name"][5])
persons_details[1]["family_details"]["children"].insert(1,{"name":"x","age":3})
# how can i access John's pets
# print (persons_details[1]["famil_details"]["wife_details"]["age"])
# # How can i access John's second childs age

# print (persons_details[1]["family_details"]["children"][1]["age"])

# access the first dictionary from the list
# print (persons_details[1])

# add the third person details
persons_details.append({})

persons_details[2] = {
                        "name":"Jane",
                        "age":32,
                        "married":False,
                        "pets":None,
                        "height":176.34,
                }



# ---------------- IGNORE THIS CODE PART -----------
# accessing the whole list
# for list_element in persons_details:
#     print (list_element)
# --------------- END OF CODE ----------------------

# list_variable = ["name",2,3.2,True,None]


# dictionary_variable = {
#                         0:1,
#                         1:2,
#                         2:3,
#                         3:4

#                     }

# print (type())
