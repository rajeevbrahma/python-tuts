import customer_operations,transactions


while True:
    choice = int(input("Select options 1. add, 2. update, 3. read, 4. delete"))
    if (choice == 1):
        customer_operations.add_customer()
    elif(choice == 2):
        rtn = transactions.authentication()
        if (rtn[0]):
            customer_operations.update_customer(rtn[1])
        else:
            print (rtn[1])
    elif(choice == 3):
        rtn = transactions.authentication()
        if (rtn[0]):
            customer_operations.get_customer(rtn[1])
        else:
            print (rtn[1])

    else:
        print ("invlid operation")

# lets run this in loop to add atleast 2 users 
# then please modify user 1 password
