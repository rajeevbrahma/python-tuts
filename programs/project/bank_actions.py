# add customer

# get customer 

# update customer 

# delete customer 
"""
    Customer Data model 

            1234:{   
                            "name":"Mark",      # only characters no symbols
                            "dob":"",           # dd-mm-yyyy
                            "account_number":1234, # integer only
                            "password":0000,    #4 digit number
                            "balance":43,       # integer only
                            "address":{},       # door no, street, city, pincode
                            "ssn":12345         # 5 digit number
                        
                    }

"""
import datetime 

customer_information = {}

last_account_number = 45390   # 5 digit number

# pincode, ssn, dob, name 

def customer_info_validation(pincode,ssn,dob,name):
    
    for symbol in ["_",",",".","1","2","3","4","5","6","7","8","9","0"]:
        if (symbol in name):
            return False,"Name contains symbol or number"
    
    if len(ssn) != 5:
        return False,"invalid ssn"

    elif len(dob.split("-")) != 3:
        return False,"Invalid date"
        
    elif len(dob.split("-")[0]) != 2 or int(dob.split("-")[0]) > 30:
    
        return False,"Invalid date or date out of range"
    
    elif len(dob.split("-")[1]) != 2 or int(dob.split("-")[1]) > 12:
        return False,"Invalid month or month out of range"
    
    elif len(dob.split("-")[2]) != 4 or (datetime.date.today().year - int(dob.split("-")[2]) < 18):
        return False,"Invalid year or less than 18 years"

    elif (len(pincode) != 3):
        return False,"invalid pincode"
    else:
        return True,None




def address():
    door_no = input("Door no ")
    street = input("Street ")
    city = input("City ")
    pincode = input("Pincode ")   # 3 digit

    return {"door_no":door_no,"street":street,"city":city,"pin":pincode}

def add_customer():
    global last_account_number
    print ("Custome info here .... ")
    name = input("Name ")
    dob = input("Date of birth ")
    password = 9999
    account_number = last_account_number 
    initial_deposit = input("Amount here ")
    addr = address()
    ssn = input("Enter ssn ")

    validated = customer_info_validation(addr["pin"],ssn,dob,name)
    
    if (validated[0]):
        customer_information.update(
            {
                account_number:{
                                    "name":name,
                                    "dob":dob,
                                    "password":password,
                                    "balance":initial_deposit,
                                    "ssn":ssn,
                                    "address":addr

                                }
            }
        )
        last_account_number+=1
    else:
        print ("Adding customer failed",validated[1])

    print (customer_information)

def get_customer():
    pass 

def update_customer():
    pass 

def delete_customer():
    pass







