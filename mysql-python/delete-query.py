"""
python with mysql
pip install pymysql
pip show pymysql

to connect mysql:
    db_server,portno,username,password,databse_name
    localhost:3306
    root
    roottoor
    ecommerce
    """

import pymysql

# connection open for mysql
connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="roottoor",
    database="ecommerce"
)
cursor = connection.cursor()
cursor.execute("delete from user where id =2")

#commit will be called during the write operations(insert,update,delete)
connection.commit()

# always close the connection
connection.close()