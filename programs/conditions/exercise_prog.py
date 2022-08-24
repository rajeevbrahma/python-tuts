family_details = {

}

family_details.update({
            "husband":{
                        "first_name":"John",
                        "middle_name":None,
                        "last_name":"Doe",
                        "age":40,
                        "occupation":"Engineer",
                        "hobbies":["Tv","Music","Gardening","Dance"]
                        }
                    }
                )

family_details.update({
    "wife":{
        "first_name":"Jane",
        "middle_name":None,
        "last_name":"Doe",
        "age":35,
        "occupation":None,
        "hobbies":["Tv","Cooking","Craft"]
    }
})

family_details.update({
    "children":[
        {"first_name":"Shane",
        "middle_name":"Watson",
        "last_name":"Doe",
        "age":12,
        "occupation":None,
        "hobbies":["Dance","Tv"]},
        {"first_name":"Lilly",
        "middle_name":"",
        "last_name":"Doe",
        "age":5,
        "occupation":None,
        "hobbies":["Tv"]}
    ]
})

family_details.update({
    "pets":[
        {
            "name":"Oliver",
            "age":7,
            "gender":"Male"
        },
        {
            "name":"Gus",
            "age":5,
            "gender":"Male"
        }
    ]
})


# who has more number of hobbies
husband_hobbies = len(family_details["husband"]["hobbies"])
wife_hobbies = len(family_details["wife"]["hobbies"])
child_1_hobbies = len(family_details["children"][0]["hobbies"])
child_2_hobbies = len(family_details["children"][1]["hobbies"])


# solution 1
larger = 0
person_with_more_hobbies = None
if (larger>wife_hobbies):
    pass
else:
    person_with_more_hobbies = "wife"
    larger = wife_hobbies
# -------

if (larger>child_1_hobbies):  # larger 4 
    pass
else:
    person_with_more_hobbies = "child_1"
    larger = child_1_hobbies  # larger 4
# ------
if (larger>child_2_hobbies):  # larger 4
    pass
else:
    person_with_more_hobbies = "child_2"
    larger = child_2_hobbies
# -------
if (larger>husband_hobbies):
    pass    
else:
    larger = husband_hobbies   # larger 4
    person_with_more_hobbies = "husband"

print (larger,person_with_more_hobbies)


# solution 2 
if (husband_hobbies > wife_hobbies and husband_hobbies > child_1_hobbies and husband_hobbies > child_2_hobbies):
    person_with_more_hobbies = "husband"
elif(wife_hobbies > husband_hobbies and wife_hobbies > child_1_hobbies and wife_hobbies > child_2_hobbies):
    person_with_more_hobbies = "wife"
elif(child_1_hobbies > husband_hobbies and child_1_hobbies > wife_hobbies and child_1_hobbies > child_2_hobbies):
    person_with_more_hobbies = "child 1"
elif(child_2_hobbies > husband_hobbies and child_2_hobbies>wife_hobbies and child_2_hobbies >child_1_hobbies):
    person_with_more_hobbies = "child 2"
else:
    print ("None")

print(person_with_more_hobbies)

# who doesnt has the middle name

people_who_doesnt_has_middle_name = []
if (family_details["husband"]["middle_name"] == None):
    people_who_doesnt_has_middle_name.append(family_details["husband"]["first_name"])
if (family_details["wife"]["middle_name"] == None):
    people_who_doesnt_has_middle_name.append(family_details["wife"]["first_name"])
if (family_details["children"][0]["middle_name"] == None):
    people_who_doesnt_has_middle_name.append(family_details["children"][0]["first_name"])
if (family_details["children"][1]["middle_name"] == None):
    people_who_doesnt_has_middle_name.append(family_details["children"][1]["first_name"])

print (people_who_doesnt_has_middle_name)

# who is younger oliver or Gus ?

if (family_details["pets"][0]["age"] < family_details["pets"][1]["age"]):
    print (family_details["pets"][1]["name"])
else:
    print(family_details["pets"][0]["name"])


# Are both the pets Male or Female ? 
# [Note: Please correct the following incase if you have one male and female dog in the family details]
if (family_details["pets"][0]["gender"] == "Male" and family_details["pets"][1]["gender"] == "Male"):
    print ("Both are Male")
else:
    print ("Both are FeMale")




