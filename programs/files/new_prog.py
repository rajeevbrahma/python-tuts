
"""
    modes

        r - read only 
        rb - read in binary format 
        r+ read and write 
        rb+ read and write in binary format 
        w - write only 
        wb - write in binary 
        wb+ - writing and reading in binary
        a+ append 
        ab+ append and read in binary 


"""

# new file 

from codecs import utf_7_encode


file_name = open("book.txt","wb")

print ("Name of the file: ", file_name.name)
print ("Closed or not : ", file_name.closed)
print ("Opening mode : ", file_name.mode)
file_name.close()


with open("book.txt","w") as file_name:
    print ("Name of the file: ", file_name.name)
    print ("Closed or not : ", file_name.closed)
    print ("Opening mode : ", file_name.mode)

with open("book.txt","w") as file_name:

    file_name.write( "HelloWorld.\nWelcome!!\n")

with open("book.txt","wb") as file_name:

    file_name.write( bytes(1234))
