
import mysql.connector 

mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pradaap@6868",
    database="db3"
)

mycurzor = mydb.cursor()
'''mycurzor.execute("SELECT * FROM actor")
result=mycurzor.fetchone()
for i in result:
    print(i)'''
#mycurzor.execute("CREATE TABLE users(username varchar(20), email varchar(30))")
'''
insert_query = ("INSERT INTO users "
               " (username, email)"
               " VALUES (%s, %s)")
values = ('john_doe', 'john@example.com')
mycurzor.execute(insert_query, values)'''

try:
    mycurzor.execute("INSERT INTO users (username,email) VALUES (%s, %s)" , ("john_doe","john@example.com"))
    mydb.commit()
    print(mycurzor.rowcount, "record inserted.")
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
'''
print("The users are :")
mycurzor.execute("SELECT * FROM users") 
result = mycurzor.fetchall() 
for row in result: 
    print(row)
'''

'''mycurzor.execute("SELECT * FROM student_details")
result = mycurzor.fetchall()
for i in result:
    print(i)'''


'''mycurzor.execute("SHOW TABLES")

for i in mycurzor:
    print(i)'''
#mycurzor.execute("CREATE TABLE Student_Details(Id varchar(5),Name varchar(20),MailId varchar(30))")
#mycurzor.execute("INSERT INTO TABLE Student_Details VALUES("101","Vishnu Balaji","vishnu123@gmail.com")")
'''mycurzor.execute("SELECT * FROM your_table")
result = mycurzor.fetchall()

for row in result:
    print(row)
'''