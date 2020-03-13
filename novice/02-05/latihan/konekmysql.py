import mysql.connector as mariaDB

mariadb_connection = mariaDB.connect(user = 'root',
password = "1untuksemua",
database="toko")
cursor = mariadb_connection.cursor()

if mariadb_connection.is_connected:
    print("mariadb sudah connect")

#cursor.execute("SELECT Pembeli, banyak, alamat * FROM satuan WHERE Pembeli= %s"(3,))