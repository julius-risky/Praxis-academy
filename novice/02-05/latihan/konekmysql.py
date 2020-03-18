import mysql.connector

mariadb_connection = mysql.connector.connect(
host="localhost",
user = "root",
password = "1untuksemua",
database="toko")
cursor = mariadb_connection.cursor()

cursor.execute("SELECT * FROM satuan")

my_result = cursor.fetchall()

for x in my_result:
    print(x)

#if mariadb_connection.is_connected:
 #   print("mariadb sudah connect")