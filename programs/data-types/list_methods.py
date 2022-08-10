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

# day - 8 
python_batch_details[0] = "This list is about the Python class Details" 

python_batch_details.extend(["8:30PM to 10:00PM EST"])

python_batch_details.extend([["8:30PM to 10:00PM EST","6:00AM to 7:30PM IST"]])

print (python_batch_details.index(instructor_details))

python_batch_details.reverse()

python_batch_details.pop()
python_batch_details.pop(1)



python_batch_details[0:2] = ["sample value"]
# python_batch_details[0:] = ["sample value"]

another_python_batch_details_variable = python_batch_details.copy()


print ([1,2,3,4]+[5,6,7])

# please ignore this following code ------------
for index,list_element in enumerate(python_batch_details):
    print (f" INDEX = {index}, LIST ELEMENT = {list_element} \n")
# --------------- end of code -----

print (another_python_batch_details_variable)

