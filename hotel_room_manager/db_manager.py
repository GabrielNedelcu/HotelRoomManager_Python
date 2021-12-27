import mysql.connector
from mysql.connector import Error
from hotel_room_manager.reservation import CReservation
from hotel_room_manager.room import CRoom
from hotel_room_manager.client import CClient
import hotel_room_manager.query_definition as qd

from flask import flash

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class CDbManager:
    _conn = None
    _cursor = None

    # Default constructor
    def __init__(self):
        # Init the connection to the database
        self.init_connection()

    # Connect to the database
    def init_connection(self):
        try:
            print('Connecting to hotel_manager...')
            self._conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="a123321",
                database="hotel_manager")

            if self._conn.is_connected():
                logging.info(' * Connection is UP')
                # If the connection is established, init the cursor
                self._cursor = self._conn.cursor()
            else:
                logging.info(' * Connection FAILED')
        except Error as e:
            logging.debug(" * " + e)

    # Check the connection
    def check_connection(self):
        if self._conn.is_connected():
            logging.info(' * Connection is UP')
        else:
            logging.info(' * Connection is DOWN')

    # Add a room to the database
    def add_room(self, room):
        # Get the data from the object
        room_data = room.get_room_data()
        # Check if the data is not empty
        if room_data != None:
            try:
                # Execute the query
                self._cursor.execute(qd.INSERT_ROOM_QUERY, room_data)
                # Commit the change to the db
                self._conn.commit()
                # Flash success message
                flash('Room succesfully added!', category='success')
            except mysql.connector.IntegrityError as err:
                logging.debug(" * SQL Error: {}".format(err))
                # Flash error message
                flash('SQL Error!', category='error')
        else:
            logging.debug(" * Room Data is NULL!! Please DEBUG!!")

    # Add a client to the database
    def add_client(self, client):
        # Get the data from the object
        client_data = client.get_client_data()
        # Check if the data is not empty
        if client_data != None:
            try:
                # Execute the query
                self._cursor.execute(qd.INSERT_CLIENT_QUERY, client_data)
                # Commit the change to the db
                self._conn.commit()
                # Flash success message
                flash('Client succesfully added!', category='success')
            except mysql.connector.IntegrityError as err:
                logging.debug(" * SQL Error: {}".format(err))
                # Flash error message
                flash('SQL Error!', category='error')
        else:
            logging.debug(" * Client Data is NULL!! Please DEBUG!!")

    # Add a reservation to the database
    def add_reservation(self, reservation):
        # Get the data from the object
        reservation_data = reservation.get_reservation_data()
        # Check if the data is not empty
        if reservation_data != None:
            try:
                # Execute the query
                self._cursor.execute(
                    qd.INSERT_RESERVATION_QUERY, reservation_data)
                # Commit the change to the db
                self._conn.commit()
                # Flash success message
                flash('Reservation succesfully added!', category='success')
            except mysql.connector.IntegrityError as err:
                logging.debug(" * SQL Error: {}".format(err))
                # Flash error message
                flash('SQL Error!', category='error')
        else:
            logging.debug(" * Reservation Data is NULL!! Please DEBUG!!")

    # Get all the rooms from the db
    def get_all_rooms(self):
        rooms_data = None
        try:
            # Execute the query
            self._cursor.execute(qd.GET_ALL_ROOMS)
            # Fetch all the data
            rooms_data = self._cursor.fetchall()
            # Check if the retrieved data is not empty
            if rooms_data != None:
                return rooms_data
            else:
                logging.debug(" * Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get all the clients from the db
    def get_all_clients(self):
        clients_data = None
        try:
            # Execute the query
            self._cursor.execute(qd.GET_ALL_CLIENTS)
            # Fetch the data
            clients_data = self._cursor.fetchall()
            # Check if the retrieved data is not empty
            if clients_data != None:
                return clients_data
            else:
                logging.debug(' * Clients Data is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get a list of all client id & names
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
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get a list of all room numbers & id
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
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get the room data for a given id
    def get_room_at_id(self, id):
        logging.info(' * Getting room data at ID = %s' % id)
        room = None
        data_set = None
        try:
            self._cursor.execute(qd.GET_ROOM_AT_ID % id)
            data_set = self._cursor.fetchall()
            if data_set != None:
                room = CRoom()
                room.construct_from_db_data(data_set)
                return room
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Delete a given(by id) room
    def delete_room(self, id):
        logging.info(' * Deleting the room with the ID = %s' % id)
        try:
            self._cursor.execute(qd.DELETE_ROOM % id)
            self._conn.commit()
            flash('Room deleted succesfully!', category='success')
            logging.info(' * Room deleted SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Update the room with the given id with the data from the given room
    def update_room(self, id, room):
        logging.info(' * Updating the room with the ID = %s' % id)
        room_data = room.get_room_data()
        try:
            self._cursor.execute(qd.UPDATE_ROOM %
                                 (room_data['room_number'], room_data['floor'], room_data['room_price'], room_data['room_type'], int(room_data['smoking'] == True), id))
            self._conn.commit()
            flash('Room updated succesfully!', category='success')
            logging.info(' * Room updated SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get all reservations made for the given room
    def get_room_reservation_history(self, idroom):
        logging.info(
            ' * Getting the reservation history for the room with the ID = %s' % id)
        try:
            self._cursor.execute(qd.SELECT_RESERVATIONS_FOR_ROOM % idroom)
            data_set = self._cursor.fetchall()
            logging.info(
                ' * History fetched SUCCESSFULLY - %d records' % len(data_set))
            return data_set
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get the data for a given client
    def get_client_at_id(self, id):
        logging.info(' * Getting client data at ID = %s' % id)
        client = None
        try:
            self._cursor.execute(qd.GET_CLIENT_AT_ID % id)
            data_set = self._cursor.fetchall()
            if data_set != None:
                client = CClient()
                client.construct_from_db_data(data_set)
                return client
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get all reservations made by the given client
    def get_client_reservation_history(self, idclient):
        logging.info(
            ' * Getting the reservation history for the client with the ID = %s' % id)
        try:
            self._cursor.execute(qd.SELECT_RESERVATIONS_FOR_CLIENT % idclient)
            data_set = self._cursor.fetchall()
            logging.info(
                ' * History fetched SUCCESSFULLY - %d records' % len(data_set))
            return data_set
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Update the given client with the data from the new client
    def update_client(self, id, client):
        logging.info(' * Updating the client with the ID = %s' % id)
        client_data = client.get_client_data()
        try:
            self._cursor.execute(qd.UPDATE_CLIENT %
                                 (client_data['name'], client_data['surname'], client_data['birthday'], client_data['adress'], client_data['cnp'], client_data['email'], client_data['phone'], id))
            self._conn.commit()
            flash('Client updated succesfully!', category='success')
            logging.info(' * Client updated SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Delete the given client
    def delete_client(self, id):
        logging.info(' * Deleting the client with the ID = %s' % id)
        try:
            self._cursor.execute(qd.DELETE_CLIENT % id)
            self._conn.commit()
            flash('Client deleted succesfully!', category='success')
            logging.info(' * Client deleted SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get all the reservations from the db
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
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Delete a given reservation
    def delete_reservation(self, id):
        logging.info(' * Deleting the client with the ID = %s' % id)
        try:
            self._cursor.execute(qd.DELETE_RESERVATION % id)
            self._conn.commit()
            flash('Reservation deleted succesfully!', category='success')
            logging.info(' * Reservation deleted SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    # Get the data from a given reservation id
    def get_reservation_at_id(self, id):
        logging.info(' * Getting reservation data at ID = %s' % id)
        reservation = None
        try:
            self._cursor.execute(qd.GET_RESERVATION_AT_ID % id)
            data_set = self._cursor.fetchall()
            if data_set != None:
                reservation = CReservation()
                reservation.construct_from_db_data(data_set)
                return reservation
            else:
                logging.debug(' * Data Set is NULL!!! Please DEBUG!!')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    def update_reservation(self, id, reservation):
        logging.info(' * Updating the reservation with the ID = %s' % id)
        reservation_data = reservation.get_reservation_data()
        try:
            self._cursor.execute(qd.UPDATE_RESERVATION %
                                 (reservation_data['idroom'], reservation_data['idclient'], reservation_data['start_date'], reservation_data['end_date'], reservation_data['parking'], reservation_data['breakfast'], reservation_data['dinner'], id))
            self._conn.commit()
            flash('Reservation updated succesfully!', category='success')
            logging.info(' * Reservation updated SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

    def set_room_next_avaliable_date(self, id, date):
        logging.info(
            ' * Setting the next avaliable date to %s for the room with the ID = %s' % (date, id))
        try:
            self._cursor.execute(qd.SET_ROOM_NEXT_DATE %
                                 (date, id))
            self._conn.commit()
            logging.info(' * Next avaliable date updated SUCCESSFULLY')
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')
