import csv 

with open('example.csv','r') as file:
    print (file)

    for row in file:
        print (row[1])

with open('example.csv','r') as file:
    csv_reader = csv.reader(file,delimiter=",")

    for row in csv_reader:
        print (row[1])

with open('example.csv','r') as file:
    csv_reader = csv.DictReader(file,delimiter=",")

    for row in csv_reader:
        print (row["Language"])

