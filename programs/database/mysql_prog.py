import mysql.connector

class Mysql:

    host = None     # class variable
    port = None     # class variable
    
    def __init__(self,database,password,user,table):
        self.database = database 
        self.user = user                    # normal
        self.__password = password          # private
        self.table = table
        self.connect()
    def connect(self):
        self.dbConnection = mysql.connector.connect(
                                            host=self.host,
                                            user=self.user,
                                            password=self.__password,
                                            database=self.database,
                                            port=self.port,
                                            autocommit=True
                                        )
        # prepare a cursor object using cursor() method
        self.cursor = self.dbConnection.cursor() 
        
    def fetchDbVersion(self):
        self.cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        version = self.cursor.fetchone()
        print ("Database version : %s " % version)

    def disConnect(self):
        self.dbConnection.close() 

    def __prepareInsertQuery(self,columns,values):
        queryColumns = ""
        for col in columns:
            queryColumns+=col+","
        queryColumns = queryColumns[:-1]

        queryValues = ""
        for val in values:
            queryValues+=str(val)+","
        queryValues = queryValues[:-1]

        return queryColumns,queryValues

    def __prepareUpdateQuery(self,data):
        update_columns_values = ""
        for col,val in data:
            update_columns_values+=col+"="+str(val)+","
        update_columns_values = update_columns_values[:-1]

        return update_columns_values        

    def create(self,columns,values):
        queryColumns,queryValues = self.__prepareInsertQuery(columns,values)
        query = f"INSERT INTO {self.table} ({queryColumns}) VALUES ({queryValues});"
        print (query)
        self.cursor.execute(query)
        
    def read(self):
        self.cursor.execute(f"SELECT * FROM {self.table};")
        result = self.cursor.fetchall() 
        for doc in result:
            print (doc)

    def readById(self,id):
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE account_number={id};") 
        result = self.cursor.fetchone()
        print (result)

    def update(self,id,data):
        self.update_columns_values = self.__prepareUpdateQuery(data)
        print (self.update_columns_values)
        self.cursor.execute(f"UPDATE {self.table} SET {self.update_columns_values} WHERE account_number={id};") 
        
    def delete (self,id):
        self.cursor.execute(f"DELETE FROM {self.table} WHERE account_number={id};") 



# Mysql.host = '127.0.0.1'
# Mysql.port = 3307

# database = 'python_bank'
# password = 'pMac'
# user = 'root'
# table = 'customer'

# sql = Mysql(database,password,user,table)


# sql.connect()
# sql.fetchDbVersion()


# columns = ['account_number','name','balance']
# values = [2,"'Josh'",10000]

# data = [('balance',999)]  #('name',"'changedname'")

# # sql.create(columns,values)
# # sql.read()
# # sql.readById(2)
# # sql.update(2,data)
# # sql.readById(2)
# # sql.delete(2)
# # sql.read()

# database = 'onemore_bank'
# password = 'pMac'
# user = 'root'
# table = 'customer'

# b2 = Mysql(database,password,user,table)
# b2.connect()
# b2.fetchDbVersion()


# b2.create(columns,[3,"'Paul'",90000])
# # b2.create(columns,[2,"'Harsha'",80000])

# b2.read()

