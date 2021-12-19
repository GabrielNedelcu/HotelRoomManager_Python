from flask import Blueprint
from flask import render_template
from flask import request
from hotel_room_manager.client import CClient
from hotel_room_manager.reservation import CReservation

from hotel_room_manager.room import CRoom

from .db_manager import CDbManager

routes = Blueprint('routes', __name__)

data_manager = CDbManager()


@routes.route('/')
@routes.route('/home')
def home():
    return render_template("home.html")


@routes.route('/view-rooms', methods=['POST', 'GET'])
def view_rooms():
    all_rooms = data_manager.get_all_rooms()
    table_headings = ("ID", "Room Number", "Floor", "Price per Night", "Room Type",
                      "Smoking allowed", "Next avaliable date", "View Room", "Delete Room")
    print(all_rooms)
    return render_template("all_rooms.html", data=all_rooms, headings=table_headings)


@routes.route('/view-clients', methods=['POST', 'GET'])
def view_clients():
    all_clients = data_manager.get_all_clients()
    table_headings = ("ID", "Name", "Surname", "Birthday", "Adress", "CNP", "Email",
                      "Phone", "Picture", "View Client", "Delete Client")
    return render_template("all_clients.html", data=all_clients, headings=table_headings)


@routes.route('/view-reservations', methods=['POST', 'GET'])
def view_reservations():
    all_reservations = data_manager.get_all_reservations()
    return render_template("all_reservations.html", data=all_reservations, headings=table_headings)


@routes.route('/client-profile')
def view_client_profile():
    return render_template("client_profile.html")


@routes.route('/room-profile')
def view_room_profile():
    return render_template("room_profile.html")


@routes.route('/add-client', methods=['POST', 'GET'])
def add_client():
    # Get client data from form
    client = CClient(request.form)
    data_manager.add_client(client)

    return render_template("insert_client.html")


@routes.route('/add-room', methods=['POST', 'GET'])
def add_room():
    # Get room data from form
    room = CRoom(request.form)
    data_manager.add_room(room)
    return render_template("insert_room.html")


@routes.route('/make-reservation', methods=['POST', 'GET'])
def add_reservation():
    # Get reservation data from form
    reservation = CReservation(request.form)
    all_clients = data_manager.get_client_id_to_name()
    all_rooms = data_manager.get_room_id_to_number()
    print(all_clients)
    data_manager.add_reservation(reservation)
    return render_template("make_reservation.html", clients_combo_name="client_id", rooms_combo_name="room_id", clients_combo_data=all_clients, rooms_combo_data=all_rooms)
