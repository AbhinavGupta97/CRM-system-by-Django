import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'store8000'
)

cursorObject = dataBase.cursor()

cursorObject.execute('SHOW DATABASES')

for x in cursorObject:
    print(x)