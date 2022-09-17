
"""

    How to read/write to .txt and .csv files 

open - to open a file in a specific mode will also used 
       to create a file when file doesnt exist


as   - aliasing purponse


modes

        r - read only 
        rb - read in binary format 
        r+ read and write 
        rb+ read and write in binary format 
        w - write only 
        w+ - write and read
        wb - write in binary 
        wb+ - writing and reading in binary
        a+ append 
        ab+ append and read in binary 
        x - create a file
        x+ - create and write to a file




"""

# Open/create a file 

# file = open("book.txt",'w+')

# file.writelines("dfasdfasd,asdfasd,fas,dfa,sdf,asdf,asdf,asd,fa,sd")

# cursor = file.tell()

# print (cursor)

# file.seek(0,0)
# cont = file.read(2)
# print (cont)

# cursor = file.tell()
# print (cursor)

# file.seek(2,0)   # argument 1 - where to start in a file, argument 2 - 0,1,2 
#                                                                     # 0 - from the begining
#                                                                     # 1 - where your cursor is
#                                                                     # 2 - from the end

# file.write("abcdef")

# # # file.seek(0,0)
# # # content = file.read(20)
# # # print (content)

# file.close()


file = open("book.txt",'w+')

file.writelines(["a","b","c"])
# (["dfasdfasd,asdfasd,fas,dfa,sdf,asdf,asdf,asd,fa,sd")

file.close()
