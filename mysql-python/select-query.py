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

try:
    # connection open for mysql
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="rooot",
        passwd="roottoor",
        database="ecommerce"
    )
    cursor = connection.cursor()
    cursor.execute("select * from user")
    for row in cursor.fetchall():
        print(row)

    # always close the connection
    connection.close()

except Exception as e:
    print("Error ",str(e))