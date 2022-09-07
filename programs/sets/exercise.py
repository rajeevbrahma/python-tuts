

# a,b
# a is populated with list of duplicates
# b should have unique elements from the list of duplicates
# loop through the list a 
# for every element add that in the list b and before that please check if the element exists in the list b or not
# if exists continue 
# if not add it

b = []
c = 1

# for element in a:
#     if (a.count(element) > 1):
#         continue
#     b.append(element)
# print (b)


# a = [1,1,2,3,4]

a = [1,1,2,3,2,2,3,4,5,6,67,4,3,2,3,4,5,7,5,3,2,23,4,4,3,2,1,3]

for i in a:
    count = 0
    for j in a:
        if (i == j):
            count+=1
    if count == 1 :
        b.append(i)

print (b)







# b = []
# for element in a:
#     if element in b:
#         continue
#     b.append(element)
# # print (b)

# print (set(a))