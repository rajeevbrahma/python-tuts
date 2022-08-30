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

# a = {"a":"1","b":"2"}

a = [1,2,3,4,5]
            
for i in a:
    pass
    # print (i)


# range(start_index,stop_index+1,step)
for index_number in range(0,len(a)): 
    # print (a[index_number])
    pass

dict_variable = {"a":1,"b":2,"c":3,"d":4}

# for key_name in dict_variable:
#     print (dict_variable.keys())
#     print (dict_variable[key_name])
#     print (dict_variable.get(key_name))

for key_name,value_name in dict_variable.items(): 
    pass
    # print (key_name,"-----",value_name)



for dict_item in dict_variable.items():
    # print (dict_item)
    key_name,value_name = dict_item
            # or 
    # key_name = dict_item[0]
    # value_name = dict_item[1]
    # print (key_name,"-------",value_name)

# for _ in range(5):
#     print (_)
#     print (type(_))
# print(_)


a = [1,2,3,4,5,5,6]


"""

while(<Tue>):   expx = a in "Oython" | a == b | a is b
    print ("welcome")

a = True

while(a):
    print ("welcom")    
    a = False

"""

i = 0
a = "Python"

# 8<10 and None == "Python"
while(i<10 and a == "Python"):
    
    print ("iteration - ",i,type(i<10),i<10,a)
    # i = 7
    if (i > 5):
        a = None
    print ("after condition check",i,type(i<10),i<10,a)
    i+=1 # 7
    print ("after i increment",i,type(i<10),i<10,a,"\n")

print ("OUT OF LOOP")
print (i,type(i<10),i<10,a)


for i in range(10):
    if (i == 5):
        continue

    print (i)

# ------------ SRIHARSHA SUGGESTION CODE BLOCK -----------
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 50, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict2,**dict1}
print ("sriharsha",dict3)

dict3 = {}
dict3.update(dict1)
dict3.update(dict2)

print (dict3)

print (id(dict1))
print (id({**dict1}))
# ----------------------

# give me even numbers using continue while looping through 0 to 100

even_numbers = []
even_numbers_dict = {}
index_variable = 1

for i in range(1,100):
    if (i%2 != 0):
        continue
    print (i,index_variable)
    even_numbers_dict.update({index_variable:i})
    index_variable +=1
    
    # even_numbers.append(i)

# print (even_numbers)

print (even_numbers_dict)


# {1:2,2:4,3:6 ........ 49:98}

# [{1:2,2:4,3:6 ........ 49:98},{1:102,2:104,3:106 ........ 49:198},{1:202,2:204,3:206 ........ 49:198}]




