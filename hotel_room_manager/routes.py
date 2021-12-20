from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
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
    return render_template("all_rooms.html", data=all_rooms, headings=table_headings, view_redirect_page="/room-profile", delete_redirect_page="/delete-room")


@routes.route('/view-clients', methods=['POST', 'GET'])
def view_clients():
    all_clients = data_manager.get_all_clients()
    table_headings = ("ID", "Name", "Surname", "Birthday", "Adress", "CNP", "Email",
                      "Phone", "Picture", "View Client", "Delete Client")
    return render_template("all_clients.html", data=all_clients, headings=table_headings, view_redirect_page="/client-profile", delete_redirect_page="/delete-client")


@routes.route('/view-reservations', methods=['POST', 'GET'])
def view_reservations():
    all_reservations = data_manager.get_all_reservations()
    return render_template("all_reservations.html", data=all_reservations, headings=table_headings)


@routes.route('/client-profile')
def view_client_profile():
    return render_template("client_profile.html")


@routes.route('/room-profile/<room_id>', methods=['POST', 'GET'])
def view_room_profile(room_id):
    floor_combo_data = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    room_type_combo_data = [
        (1, 'Single'),
        (2, 'Double'),
        (3, 'Queen'),
        (4, 'King'),
        (5, 'Twin'),
        (6, 'Suite'),
        (7, 'Appartament')
    ]

    table_headings = ["Reservation ID", "Client Name", "Client Surname", "Client Phone Number",
                      "Start Date", "End Date", "View Reservation Details", "Delete Record"]
    if request.method == "POST":
        room_obj = CRoom()
        room_obj.construct_from_form_data(request.form)
        data_manager.update_room(room_id, room_obj)

    reservation_history = data_manager.get_room_reservation_history(room_id)
    room = data_manager.get_room_at_id(room_id)
    room_data = room.get_room_data()
    selected_floor = room_data['floor'] - 1
    selected_room_type = int(room_data['room_type'] or 0) - 1
    print(room.get_room_data())

    return render_template("room_profile.html",
                           room_data=room.get_room_data(),
                           floor_combo_label_text="Floor", floor_combo_name='room_floor', floor_combo_data=floor_combo_data, floor_selected_option=selected_floor,
                           type_combo_label_text="Room Type", type_combo_name='room_type', type_combo_data=room_type_combo_data, type_selected_option=selected_room_type,
                           headings=table_headings, data=reservation_history, view_redirect_page='/view-reservations', delete_redirect_page="/delete-reservation")


@routes.route('/delete-room/<room_id>', methods=['POST', 'GET'])
def delete_room(room_id):
    data_manager.delete_room(room_id)
    return redirect('/view-rooms')


@routes.route('/add-client', methods=['POST', 'GET'])
def add_client():
    # Get client data from form
    client = CClient(request.form)
    data_manager.add_client(client)

    return render_template("insert_client.html")


@routes.route('/add-room', methods=['POST', 'GET'])
def add_room():
    # Get room data from form
    room = CRoom()
    room.construct_from_form_data(request.form)
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
    return render_template("make_reservation.html",
                           clients_combo_label_text="Clients", clients_combo_name="client_id", clients_combo_data=all_clients, clients_selected_option=-1,
                           rooms_combo_label_text="Rooms", rooms_combo_name="room_id", rooms_combo_data=all_rooms, rooms_selected_option=-1)
