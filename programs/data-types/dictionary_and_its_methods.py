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

 