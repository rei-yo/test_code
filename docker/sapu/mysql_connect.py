import mysql.connector

cnx = mysql.connector.connect(
    user = "root",
    password = "adminadmin",
    host = "localhost",
    port = "13306"
)

cursor = cnx.cursor()
cursor.execute("SELECT * FROM test_db.users")

for id, name in cursor:
    print(f'{id}:{name}')