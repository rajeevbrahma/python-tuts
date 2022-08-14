"""

    We can store the data in key value pairs.They are changeable and duplicates are not allowed
    example :{
        key:value
    }
    "key"   - allowed data types : numbers,strings
    "value" - allowed data types : numbers,strings,lists,dictionaries,boolean,none



    A Dictionary will have 
            word : and its respective meaning

    Like the same way dictioinaries in Python will be have 
        key_name : and its associated value

    How can we relate dictionaries with List

    In list we associate list elements with the index and dictionaries we associate
    dictionary values with keys.

    In list we are accessing list elements with its respective index number
    In dictionary we can access values with its respective key name

   Symbol ":" (colon) will be used to seperate key and its value

   In List we seperate each element with symbol ","(comma) In the same way we 
   seperate dictionary elements using same symbol "," (comma) 
  
  List Example:
        ["Name","Lastname",20,123,20]
            0       1      2   3   4

    Example:
        dictionary_variable = {
                                "first_name":"Paul"
                                "last_name":"K"
                                "age":34
                                "height":122
                                "weight":34
                            }

"""

# dictionary variable definition
dictionary_variable = {
                        "first_name":"X",
                        "age":34,
                        "height":122,
                        "weight":34,
                        "marital_status":True,
                        "any_pets":None,
                        "no_of_children":2
                    }


# To print the whole dictionary
print (dictionary_variable)

# When you want to access value 34 from the above dictionary
print (dictionary_variable["age"])

 
"""
 
    Dictionary Methods
    
        >>> a = {"name":"Mark","age":40,"Degree":"MS"}

    -- copy()

        >>> b = a.copy()
        >>> b
        {'name': 'Mark', 'age': 40, 'Degree': 'MS'}
    
    -- get()

        >>> a.get('name')
        'Mark'
        >>> a.get('age')
        40
        >>> a.get('Degree')
        'MS'

    -- items()
        >>> a.items()
        dict_items([('name', 'Mark'), ('age', 40), ('Degree', 'MS')])
    
    -- keys()
        >>> a.keys()
        dict_keys(['name', 'age', 'Degree'])

    -- values()
        >>> a.values()
        dict_values(['Mark', 40, 'MS'])
    
    -- update()
        >>> a.update({"Degree":"MTech"})
        >>> a
        {'name': 'Mark', 'age': 40, 'Degree': 'MTech'}
        >>> a.update({"Job-Title":"Sr SW Engineer"})
        >>> a
        {'name': 'Mark', 'age': 40, 'Degree': 'MTech', 'Job-Title': 'Sr SW Engineer'}


    -- popitem()
        >>> a.popitem()
        ('Job-Title', 'Sr SW Engineer')
        >>> a
        {'name': 'Mark', 'age': 40, 'Degree': 'MTech'}

    -- pop()    
        >>> a.pop('Degree')
        'MTech'
        >>> a
        {'name': 'Mark', 'age': 40}
        
    -- clear() 
        >>> a.clear()
        >>> a
        {}
    
    -- setdefault()
        >>> a
        {'name': None}
        >>> a.setdefault('age')
        >>> a
        {'name': None, 'age': None}
    
    -- fromkeys()
        >>> a.fromkeys(["name","age","Degree","Job-Title"],["Mark",40,"MS","Sr SW Engineer"])
        {'name': ['Mark', 40, 'MS', 'Sr SW Engineer'], 'age': ['Mark', 40, 'MS', 'Sr SW Engineer'], 'Degree': ['Mark', 40, 'MS', 'Sr SW Engineer'], 'Job-Title': ['Mark', 40, 'MS', 'Sr SW Engineer']}
        >>> a
        {}
        >>> a.fromkeys(["name","age","Degree","Job-Title"])
        {'name': None, 'age': None, 'Degree': None, 'Job-Title': None}

    
"""