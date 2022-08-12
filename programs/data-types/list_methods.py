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



"""

        -9-8-7-6-5-4-3-2-1    
    a = [1,2,3,4,5,6,7,8,9]
         0,1,2,3,4

    a[:4]
    a[:-5]

    a[ starting number index : ending number index + 1 : step (positive/negative) ]

    a = [1,2,3,4,5,6,7,8,9]
         0,1,2,3,4,5,6,7,8   - index
         
           0,1,2,3
                 0,1,2,3
                       0,1,2,3
                           0,1,2

        1, 3,  5,  7
Paul -  0,0+2,2+2,4+2  

    a[::2]


"""

"""
    List slicing using the negative step

         -9 -8,-7,-6,-5,-4,-3,-2,-1  => Negative Index
          |  |  |  |  |  |  |  |  |
    a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
          |  |  |  |  |  |  |  |  |
          0, 1, 2, 3, 4, 5, 6, 7, 8  => Positive Index

    syntax template to slice list using negative step

    a[+ve end element index : +ve start element index : negative step]

    When you give negative step, the list will be printed in the reverse order

    Examples : 

        a[::-1]   => [8, 7, 6, 5, 4, 3, 2, 1]

        a[::-2]   => [8, 6, 4, 2]

        a[::-3]   => [8, 5, 2]

        a[:3:-1]  => [8, 7, 6, 5] : executing started at 3rd index element and printed in reverse rest of the list

        a[6:2:-1] => [7, 6, 5, 4] : execution started at 2nd index element and printed till before 6th index in the list


        when you have negative index numbers with negative step then template will be

        a[ -v start element index  : -ve end element index : negative step]


        a[-1::-1]
            [8, 7, 6, 5, 4, 3, 2, 1] : execution started from -1 index element till rest of the list in reverse order with -1 step
        a[-2::-1]
            [7, 6, 5, 4, 3, 2, 1]    : execution started from -2 index element till rest of the list in reverse order with -1 step
        a[-3::-1]
            [6, 5, 4, 3, 2, 1]      : execution started from -3 index element till rest of the list in reverse order with -1 step
        a[-4::-1]
            [5, 4, 3, 2, 1]         : execution started from -4 index element till rest of the list in reverse order with -1 step

        a[-1:-7:-1]
            [8, 7, 6, 5, 4, 3]      : execution started from -1 index element till -7 index element with -1 step

        a[-1:-6:-1]
            [8, 7, 6, 5, 4]         : execution starte from -1 index element till -6 index element with -1 step


"""


