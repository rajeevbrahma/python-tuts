python_batch_details = [
    ["x","y",10,["z","a","b"],["masters"]],
    ["x","y",10,["z","a","b"],["masters"]],
    ["x","y",10,["z","a","b"],["masters"]],

]

fourth_person_details = ["x","y",8,["rick","john","yes"],["masters"]]



# pybde = [[],[],[],3,False]

python_batch_details.append(fourth_person_details)
python_batch_details.append(4)
python_batch_details.append(True)

python_batch_details.insert(0,"Instructor")

python_batch_details.insert(1,"Python")

instructor_details = ["instructor","asdf",[],[]]

# instructor_details.insert(2,20)

python_batch_details.insert(2,instructor_details)

python_batch_details[2].insert(2,20)

python_batch_details[3][3].insert(1,"Rick")



# please ignore this following code ------------
# ,"-----> ",python_batch_details.index(list_element),"\n"
for list_element in python_batch_details:
    print (list_element,"\n")
# --------------- end of code -----


# [python-tuts-[programs-[data-types-[list_mehtods.py]]]]










# #  EXAMPLE 2 :
# list_variable = ["apple","bat","cat","dog"]

# list_variable.append("elephant")

# print (list_variable)

# new_list_variable = list_variable.copy()

# print (new_list_variable)

# print (list_variable.count("cat"))

# list_variable.extend(["fan","goat"])
# print (list_variable)

# print (list_variable.index("goat"))

# list_variable.insert(1,"ball")

# print (list_variable)

# list_variable.pop(2)
# print (list_variable)

# list_variable.remove("ball")

# print (list_variable)

# list_variable.reverse()
# print (list_variable)

# list_variable.sort()
# print (list_variable)

# list_variable[1] = "ant"
# print (list_variable)

# list_variable[2:4] = ["bank","car"]
# print (list_variable)

# print ([1,2,3,4]+[5,6,7])