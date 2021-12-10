import mysql.connector
from mysql.connector import Error

class db_manager:
    
    def init_connection():
        conn = None
    try:
        print('Connecting to hotel_manager...')
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="a123321",
                    database="hotel_manager")

        if conn.is_connected():
            print('Connection established')
        else:
            print('Connection failed ...')
    except Error as e:
        print(e)