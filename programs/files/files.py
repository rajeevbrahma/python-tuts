
# Open a file
file = open("sample.txt", "wb")
print ("Name of the file: ", file.name)
print ("Closed or not : ", file.closed)
print ("Opening mode : ", file.mode)
file.close()


# Open a file
file = open("sample.txt", "w")
file.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
file.close()


# Open a file
file = open("sample.txt", "r+")
str = file.read(10)
print ("Read String is : ", str)

# Close opened file
file.close()


# Open a file
file = open("sample.txt", "r+")
str = file.read(10)
print ("Read String is : ", str)

# Check current position
position = file.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = file.seek(0, 0)
str = file.read(10)
print ("Again read String is : ", str)

# Close opened file
file.close()
