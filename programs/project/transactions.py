"""
    authentication (accountnumber,password)
    
        deposit money (accountnumber,money)
        withdraw money (accountnumber,money)
        transfer money within the bank (accountnumber,payee account number,money)

"""

from customer_operations import customer_information

def authentication():
    # accountnumber, password
    account_number = int(input("Enter account number"))
    if account_number in customer_information:
        name = customer_information[account_number]["name"]
        print (f"Welcome {name} ....")
        password = input("Enter password")
        if password == customer_information[account_number]["password"]:
            return True,account_number
        else:
            return False,"Wrong password"
    else:
        return False,"Account not found"
    

def deposit_money():
    pass 

def withdraw_money():
    pass 

def transfer_money():
    pass 


