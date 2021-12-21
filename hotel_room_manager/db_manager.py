import mysql.connector
from mysql.connector import Error
from hotel_room_manager.room import CRoom
from hotel_room_manager.client import CClient
import hotel_room_manager.query_definition as qd

import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


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
                self._cursor.execute(qd.INSERT_ROOM_QUERY, room_data)
                self._conn.commit()
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
        else:
            logging.debug(" * Room Data is NULL!! Please DEBUG!!")

    def add_client(self, client):
        client_data = client.get_client_data()
        if client_data != None:
            try:
                self._cursor.execute(qd.INSERT_CLIENT_QUERY, client_data)
                self._conn.commit()
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
        else:
            logging.debug(" * Client Data is NULL!! Please DEBUG!!")

    def add_reservation(self, reservation):
        reservation_data = reservation.get_reservation_data()
        if reservation_data != None:
            try:
                self._cursor.execute(
                    qd.INSERT_RESERVATION_QUERY, reservation_data)
                self._conn.commit()
                print("Reservation succesfully added!")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
        else:
            logging.debug(" * Reservation Data is NULL!! Please DEBUG!!")

    def get_all_rooms(self):
        rooms_data = None
        try:
            self._cursor.execute(qd.GET_ALL_ROOMS)
            rooms_data = self._cursor.fetchall()
            if rooms_data != None:
                return rooms_data
            else:
                logging.debug(" * Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_all_clients(self):
        clients_data = None
        try:
            self._cursor.execute(qd.GET_ALL_CLIENTS)
            rooms_data = self._cursor.fetchall()
            if rooms_data != None:
                return rooms_data
            else:
                logging.debug(' * Clients Data is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_client_id_to_name(self):
        data_set = None
        try:
            self._cursor.execute(qd.GET_CLIENT_ID_TO_NAME)
            data_set = self._cursor.fetchall()
            if data_set != None:
                return data_set
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_room_id_to_number(self):
        data_set = None
        try:
            self._cursor.execute(qd.GET_ROOM_ID_TO_NUMBER)
            data_set = self._cursor.fetchall()
            if data_set != None:
                return data_set
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_room_at_id(self, id):
        logging.info(' * Getting room data at ID = %s' % id)
        room = None
        data_set = None
        try:
            self._cursor.execute(qd.GET_ROOM_AT_ID % id)
            data_set = self._cursor.fetchall()
            if data_set != None:
                print(data_set)
                room = CRoom()
                room.construct_from_db_data(data_set)
                return room
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def delete_room(self, id):
        logging.info(' * Deleting the room with the ID = %s' % id)
        try:
            self._cursor.execute(qd.DELETE_ROOM % id)
            self._conn.commit()
            logging.info(' * Room deleted SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def update_room(self, id, room):
        logging.info(' * Updating the room with the ID = %s' % id)
        room_data = room.get_room_data()
        try:
            self._cursor.execute(qd.UPDATE_ROOM %
                                 (room_data['room_number'], room_data['floor'], room_data['room_price'], room_data['room_type'], int(room_data['smoking'] == True), id))
            self._conn.commit()
            logging.info(' * Room updated SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_room_reservation_history(self, idroom):
        logging.info(
            ' * Getting the reservation history for the room with the ID = %s' % id)
        try:
            self._cursor.execute(qd.SELECT_RESERVATIONS_FOR_ROOM % idroom)
            data_set = self._cursor.fetchall()
            # print("INNER")
            # print(data_set)
            logging.info(
                ' * History fetched SUCCESSFULLY - %d records' % len(data_set))
            return data_set
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_client_at_id(self, id):
        logging.info(' * Getting client data at ID = %s' % id)
        client = None
        client_set = None
        try:
            self._cursor.execute(qd.GET_CLIENT_AT_ID % id)
            data_set = self._cursor.fetchall()
            if data_set != None:
                print(data_set)
                client = CClient()
                client.construct_from_db_data(data_set)
                return client
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_client_reservation_history(self, idclient):
        logging.info(
            ' * Getting the reservation history for the client with the ID = %s' % id)
        try:
            self._cursor.execute(qd.SELECT_RESERVATIONS_FOR_CLIENT % idclient)
            data_set = self._cursor.fetchall()
            # print("INNER")
            # print(data_set)
            logging.info(
                ' * History fetched SUCCESSFULLY - %d records' % len(data_set))
            return data_set
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def update_client(self, id, client):
        logging.info(' * Updating the client with the ID = %s' % id)
        client_data = client.get_client_data()
        try:
            self._cursor.execute(qd.UPDATE_CLIENT %
                                 (client_data['name'], client_data['surname'], client_data['birthday'], client_data['adress'], client_data['cnp'], client_data['email'], client_data['phone'], id))
            self._conn.commit()
            logging.info(' * Client updated SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def delete_client(self, id):
        logging.info(' * Deleting the client with the ID = %s' % id)
        try:
            self._cursor.execute(qd.DELETE_CLIENT % id)
            self._conn.commit()
            logging.info(' * Client deleted SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def get_all_reservations(self):
        logging.info(' * Getting all the reservations')
        data_set = None
        try:
            self._cursor.execute(qd.GET_ALL_RESERVATIONS)
            data_set = self._cursor.fetchall()
            logging.info(
                ' * Reservations fetched SUCCESSFULLY - %d records' % len(data_set))
            return data_set
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
