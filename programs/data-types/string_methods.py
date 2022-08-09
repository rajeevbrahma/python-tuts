example_sentence_1 = "Python is easy to learn.  "

example_sentence_2 = "python is easy to learn"

print (example_sentence_2.capitalize())

print (example_sentence_1.casefold())

print (example_sentence_1.center(29))

print (example_sentence_1.count("e"))   # Returns the count of a char in a string

print (example_sentence_1.find("t"))    # Returns the index of a char in the string
print (example_sentence_1.index("t"))    # Returns the index of a char in the string

print (example_sentence_1.strip())     # Removes white space at begining or ending of a string 

print ("/".join(example_sentence_2))

print (example_sentence_1.replace("tough","easy"))

print ("{name} is {level} to learn".format(name="Python",level="easy"))