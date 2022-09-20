import csv 


# file = open("example.csv","r")


# with open('example.csv','r') as file:
    
#     for row in file:
#         print (row.split(",")[1])



"""
    reader  -> file rows will be stored in list [],
    DictReader -> file rows will be stored in key value pairs {}

    [[1,Python,Backend],[],[]]

    [{"s.no":1,"language":"Python","Type":"Backned"},{},{}]

"""

print ("\n CSV READER ....")
with open('example.csv','r') as file:
    csv_reader = csv.reader(file,delimiter=",")
    
    for row in csv_reader:
        print (row)
        # print (row[1])

with open('example.csv','r') as file:
    csv_reader = csv.DictReader(file,delimiter=",")

    for row in csv_reader:
        print (row)
        # print (row["Language"])



# csv.writer
with open("example.csv",'a') as file:

    row = [[4,"Kotlin","Android"],[5,"Java","Android"]]

    csv_write = csv.writer(file)

    # csv_write.writerow(row)
    # csv_write.writerows(row)


# csv.dictwriter
with open("example.csv",'a') as file:

    fields = ["s.no","Language"]
    row = [{"s.no":4,"Language":"Kotlin"},{"s.no":5,"Language":"Java"}]

    csv_write = csv.DictWriter(file,fieldnames=fields)

    # csv_write.writerow(row)
    csv_write.writerows(row)






with open("example.csv","r") as file:
    csv_reader = csv.reader(file,delimiter=",")

    for row in csv_reader:
        print (row)



# class open:

#     def __enter__(self):
#         pass 

#     def __exit__(self):
#         pass
#         file.close()