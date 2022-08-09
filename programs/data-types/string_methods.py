
example_sentence_1 = "   Python is easy to learn.  "

example_sentence_2 = "python is easy to learn"

print (example_sentence_2.capitalize())         # turns the first letter of first word into upper case

print ("PYTHON IS EASY TO LEARN".casefold())    # Returns the sentence in small letters

print (example_sentence_1.center(29))           # Add given number of spaces before the center of the string

print (example_sentence_1.count("i"))           # Returns the count of a char in a string

print (example_sentence_1.find("t"))            # Returns the index of a char in the string
print (example_sentence_1.index("t"))           # Returns the index of a char in the string

print (example_sentence_1.strip())     # Removes white space at begining or ending of a string 

print (" ".join(example_sentence_2))    # joins every character with the given character (space in this example)

print (example_sentence_1.replace("easy","super easy"))  # replace a word with the given word


print ("{name} is {level} to learn".format(name="Python",level="easy"))

print ("Hello {first_name} {last_name}! How are you ? ".format(first_name="John",last_name="K"))

first_name = "Name"
last_name = "Last Name"

print (f"Hello {first_name}, {last_name}! How are you ?")

print ("Hello %s %s How are you"%(first_name,last_name))

# %d - integers
# %f - floats
# %s - strings 

