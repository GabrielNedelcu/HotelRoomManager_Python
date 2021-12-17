import mysql.connector
from mysql.connector import Error
from hotel_room_manager.room import CRoom
from hotel_room_manager.client import CClient

INSERT_ROOM_QUERY = ("INSERT INTO rooms"
                     "(room_number, floor, room_price, room_type, smoking)"
                     "VALUES (%(room_number)s, %(floor)s, %(room_price)s, %(room_type)s, %(smoking)s)")

INSERT_CLIENT_QUERY = ("INSERT INTO clients"
                       "(name, surname, birthday, adress, cnp, email, phone)"
                       "VALUES (%(name)s, %(surname)s, STR_TO_DATE(%(birthday)s,'%m/%d/%Y'), %(adress)s, %(cnp)s, %(email)s, %(phone)s)")

GET_ALL_ROOMS = ("SELECT * FROM rooms")


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
        else:
            print("Room Data is NULL!! Please DEBUG!!")

    def add_client(self, client):
        client_data = client.get_client_data()
        if client_data != None:
            try:
                self._cursor.execute(INSERT_CLIENT_QUERY, client_data)
                self._conn.commit()
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
        else:
            print("Client Data is NULL!! Please DEBUG!!")

    def get_all_rooms(self):
        rooms_data = None
        try:
            self._cursor.execute(GET_ALL_ROOMS)
            rooms_data = self._cursor.fetchall()
            if rooms_data != None:
                return rooms_data
            else:
                print("Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
