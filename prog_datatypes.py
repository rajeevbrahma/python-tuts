'''

    integer
    string
    float

    list (array)   - position based variable
    dictionary (json/object)


'''

# LIST

list_variable = [4,4.6,'test',[3,2,3]]

details_variable = [
                    "Mark",                 # - 0
                    30,                     # - 1
                    5.6,                    # - 2
                    True,                   # - 3
                    [
                        [
                            'white',        # - 4-0-0
                            'black'
                        ],
                        [
                            'white',        # - 4-1-0
                            'black'
                        ],   
                        "New Yortk City",       # - 4-1
                        "USA"
                    ],
                    ["lucy",                    # - 5-0
                        [   
                            'john',             # - 5-1-0
                            'harry',            # - 5-1-1
                            [
                                'white',        # - 5-1-2-0
                                'black'
                            ]
                        ]
                    ]
                
                ]

print (details_variable[1:4])

print (details_variable[1:])
print (details_variable[:4])

'''
    list slice 

            [ start with this index : end before this index]


'''

'''

    Negative indexing

  a=[1,2,3,4,5,6,6,7,8]
     0,1,2,3,4,5,6,7,8    - positive index
                 -2,-1   



    a[0] => 1

'''
a = [1,2,3,4,5,6,6,7,8]

print (a[:-1])

print (len(a))

a.append('new value')

# list operations 
    # append
    # update



# ----------------- DICTIONARY --------------------

details_variable = {
    "marital_status":True,
    "name":"Mark Sr",
    "age":30,
    "height":5.6,
    "family_details":{
                        "wife":"lucy",
                        "children":[
                                        {
                                            "name":"Mark Jr",
                                            "sex":"Male",
                                            "age":10
                                        },
                                        {
                                            "name":"Maria",
                                            "sex":"Female",
                                            "age":5
                                            
                                        }
                                    ]
                    },
    }

# print (details_variable["family_details"]["children"][0]["name"])

print (type(details_variable["family_details"]["children"][0]))


# keys, values, update, other ways of intializing, looping through a dictionary 