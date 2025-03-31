import mysql.connector as mycon
db=mycon.connect (host ='localhost', user='root',
password='root', database='emp')
cur=db.cursor()
numrow=cur.execute
('Create table emp21 (empno int, name varchar(20), salary int):') 
cur.execute("Insert into emp21 values(1, 'Neha', 9000)") 
cur.execute("Insert into emp21 values (2, 'Prakash', 10000)")
cur.execute("Insert into emp21 values (3, 'Kriti', 65000)")
cur.execute("Insert into emp21 values (4, 'Raj', 11000)")
db.commit()
cur.close()
db.close()
