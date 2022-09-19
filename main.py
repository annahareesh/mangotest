import mysql.connector as connection

mydb = connection.connect(host='localhost',user = 'root', password='Daemon@12')

print(mydb)

cursor = mydb.cursor()
#cursor.execute('create database vineela')

#cursor.execute(' create table vineela.vinni(emp_id int(10), emp_name varchar(80), emp_mail varchar(20), emp_sal int(10)) ')

cursor.execute('use vineela')

cursor.execute('show tables')

print(cursor.fetchall())


