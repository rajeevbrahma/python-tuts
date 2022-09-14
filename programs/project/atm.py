import bank_actions


while True:

    choice = int(input("Select options 1. add, 2. update, 3. read, 4. delete"))
    if (choice == 1):
        bank_actions.add_customer()
    elif(choice == 2):
        bank_actions.update_customer()
    else:
        print ("invlid operation")

# lets run this in loop to add atleast 2 users 
# then please modify user 1 password
