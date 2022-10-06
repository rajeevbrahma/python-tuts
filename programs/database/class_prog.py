import mysql.connector

db = mysql.connector.connect(host='127.0.0.1',
                             user='root',
                             password='pMac',
                             database='python_bank',
                             port=3307
                             )
# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()