"""
add()	            Adds an element to the set
clear()	            Removes all the elements from the set
copy()	            Returns a copy of the set
difference()	    Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	        Remove the specified item
intersection()	    Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	    Returns whether two sets have a intersection or not
issubset()	        Returns whether another set contains this set or not
issuperset()	    Returns whether this set contains another set or not
pop()	            Removes an element from the set
remove()	        Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	            Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""


# how to define set

set_variable = set((1,2,3))
set_variable_2 = {1,2,3}
set_variable_3 = set([1,2,3])
print (type(set_variable),type(set_variable_2),type(set_variable_3))

set_variable.add(4)
set_variable.add((5,6))
# set_variable.add([7,8]) # not allowed
set_variable_2.clear()
print (set_variable_2)
print (set_variable)
print (set_variable.difference(set_variable_3))
set_variable.difference_update(set_variable_3)
print (set_variable)

set_variable.discard((5,6))

print (set_variable)
set_variable.remove(4)   # pop is also method to remove element
print (set_variable)

set_variable = set((1,2,3))
set_variable_2 = {1,2,3,4,5,6}
print (set_variable.intersection(set_variable_2))
set_variable.intersection_update(set_variable_2)
print (set_variable)
set_variable.update(set_variable_2)
print (set_variable)

set_variable.union(set_variable_2)
print (set_variable)



