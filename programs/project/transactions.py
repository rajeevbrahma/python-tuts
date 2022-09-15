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
    
def balance_check(account_number,amount):
    if (customer_information[account_number]["balance"] >= amount):
        return True
    else:
        return False

def balance_display(account_number):
    print (customer_information[account_number]["balance"])

def deposit_money(account_number,deposit_amount):
    customer_information[account_number]["balance"]+=deposit_amount 

def withdraw_money(account_number,withdraw_amount):
    if (balance_check(account_number,withdraw_amount)):
        customer_information[account_number]["balance"]-=withdraw_amount 

def transfer_money():
    # authentication
    # check for payee account in customer informatino 
    # if exists
        # payers balance we have to check
        # if enough amount to transfer
            # update payees account with the amount
            # subtract the amount from payer account information
        # else Not enough money to transfer
    # else payee doesnt exist    
    pass 


