import sqlite3
banco = sqlite3.connect('data_base.db')
cursor = banco.cursor()
cursor.execute("Create table cliente(nome text, idade integer,sex text)")
cursor.execute("INSERT INTO cliente VALUES('Cynthia',40,'f'),('pedro',20,'m')")
print(cursor.fetchall())
banco.commmit()
cursor.close()
banco.close()