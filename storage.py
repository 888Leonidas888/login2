from os import getenv
import mysql.connector
from mysql.connector import Error

class Storage:
    def __init__(self) -> None:
        self.connection = ''

    def connect(self):
        connection = mysql.connector.connect(
            host='localhost',
            database='db_login',
            user='root',
            password=getenv('mysql_pass')
        )
        self.connection = connection

    def disconnect(self):
        self.connection.close()

    def read(self):
        sql_cmd = 'select * from tb_login'
        cursor = self.connection.cursor()
        cursor.execute(sql_cmd)
        records = cursor.fetchall()
        cursor.close()
        self.disconnect()
        return records

    def validate_user(self, email, password):
        sql_cmd = 'select * from tb_login where email = %s and password = %s'
        cursor = self.connection.cursor()
        cursor.execute(sql_cmd, (email, password))
        records = cursor.fetchall()
        cursor.close()
        self.disconnect()

        if len(records) == 0:
            return False
        return True


# email = 'staff@holbertonschool.com'
# password = 'holbertonFTW'

# cnn = Storage()
# cnn.connect()
# records = cnn.validate_user(email, password)

# print(records)
