"""

    csv file

    operand1,operand_2,add,      sub,mul,div
    1           1
    2           2
    3           3
    4           4
    5           5


"""
import csv 

with open("numbers.csv","w+") as number_file:

    rows = [

        ["op1","op2","add"],
        [1,2],
        [1,2]
    ]
    
    for row in rows:
        if len(row)<3:
            print (row)
            print (rows.index(row))
            rows[rows.index(row)].append(row[0]+row[1])
    
    print (rows)

    csv_write = csv.writer(number_file,delimiter=",")
    csv_write.writerows(rows)

import csv 

with open("numbers.csv","r+") as number_file:
    
    csv_reader = csv.DictReader(number_file)

    fields = ["mul"]

    new_row = []


    for row in csv_reader:        
        new_row.append({"mul":int(row["op1"]) * int(row["op2"])})
    
    # print (row)

    # for r in csv_reader:
    #     print (r)
    print (new_row)
    csv_write = csv.DictWriter(number_file,fieldnames=fields)

    csv_write.writerows

    
