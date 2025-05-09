# for installation mysql.connector write in terminal 'pip install mysql-connector-python'
import mysql.connector 

# Connecting to sakila data base using given server and port
"""
The Sakila sample database is a fictitious database designed to represent a DVD rental store.
"""
host_db = str(input("Server: "))
password_db = str(input("Password for data base: "))

db = mysql.connector.connect(
    host = host_db,
    port = '3306',
    user = 'student',
    database = 'sakila',
    password = password_db
)

mycursor=db.cursor() 

"""
Our task:
Determine the date of the longest unpaid rental and find the phone number of the customer who has the movie
"""
sql = "SELECT \
    MAX(rental.rental_date) AS rental_date,\
    customer.customer_id,\
    address.phone \
    FROM rental,customer,address \
    WHERE rental.return_date IS NULL AND \
    rental.customer_id = customer.customer_id AND\
    customer.address_id = address.address_id \
    ORDER BY rental.rental_date ASC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

# our sql enquiry should give a table with one row and thre columns: rental_date, customer_id,phone
# So my result will be tuple with 3 elements
print('rental_date: ', myresult[0][0])
print('customer_id: ', myresult[0][1])
print('phone: ', myresult[0][2])
