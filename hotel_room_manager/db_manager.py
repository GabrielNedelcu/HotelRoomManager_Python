import mysql.connector
from mysql.connector import Error
from .room import CRoom

INSERT_ROOM_QUERY = ("INSERT INTO rooms"
                     "(room_number, floor, room_price, room_type, smoking)"
                     "VALUES (%(room_number)s, %(floor)s, %(room_price)s, %(room_type)s, %(smoking)s)")


class CDbManager:
    _conn = None
    _cursor = None

    def __init__(self):
        self.init_connection()

    def init_connection(self):
        try:
            print('Connecting to hotel_manager...')
            self._conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="a123321",
                database="hotel_manager")

            if self._conn.is_connected():
                print('Connection established ...')
                self._cursor = self._conn.cursor()
            else:
                print('Connection failed ...')
        except Error as e:
            print(e)

    def check_connection(self):
        if self._conn.is_connected():
            print('Connection is up ...')
        else:
            print('Connection is down ...')

    def add_room(self, room):
        room_data = room.get_room_data()
        if room_data != None:
            try:
                self._cursor.execute(INSERT_ROOM_QUERY, room_data)
                self._conn.commit()
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
