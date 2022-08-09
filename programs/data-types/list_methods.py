
list_variable = ["apple","bat","cat","dog"]

list_variable.append("elephant")

print (list_variable)

new_list_variable = list_variable.copy()

print (new_list_variable)

print (list_variable.count("cat"))

list_variable.extend(["fan","goat"])
print (list_variable)

print (list_variable.index("goat"))

list_variable.insert(1,"ball")

print (list_variable)

list_variable.pop(2)
print (list_variable)

list_variable.remove("ball")

print (list_variable)

list_variable.reverse()
print (list_variable)

list_variable.sort()
print (list_variable)

list_variable[1] = "ant"
print (list_variable)

list_variable[2:4] = ["bank","car"]
print (list_variable)

print ([1,2,3,4]+[5,6,7])