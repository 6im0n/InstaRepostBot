import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="xxxxxx", user='xxxxx', password='xxxxx', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS photos_instagram")

#Creating table as per requirement
sql ='''CREATE TABLE photos_instagram(
   id CHAR(20),
   path CHAR(200),
   status CHAR(10),
   owner CHAR(100)
)'''
cursor.execute(sql)
print("Table created successfully........")

#Closing the connection
conn.close()
