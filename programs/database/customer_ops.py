from mysql_prog import Mysql


customer_details = {
    "name":"'Mark'",
    "ssn":"'1234'",
    "balance":9000
}


class CustomerOps(Mysql):

    accounNumber = 1000   # class variable


    def __init__(self):
        Mysql.host = '127.0.0.1'
        Mysql.port = 3307
        database = 'chase_bank'
        password = 'pMac'
        user = 'root'
        table = 'customer'
        Mysql.__init__(self,database,password,user,table)
        self.__connect()
        

    def __accounNumberGeneration(self):
        CustomerOps.accounNumber+=1
        return CustomerOps.accounNumber
    
    def __connect(self):
        self.connect()
        self.fetchDbVersion()

    def addCustomer(self,customer_details):
        accountNumber = self.__accounNumberGeneration()
        customer_details.update({"account_number":accountNumber})
        columns = customer_details.keys()
        values = customer_details.values()
        self.create(columns,values)


cOps = CustomerOps() 
cOps.addCustomer(customer_details)    