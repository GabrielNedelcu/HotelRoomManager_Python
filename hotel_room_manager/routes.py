from datetime import datetime, timedelta
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask.helpers import flash
from hotel_room_manager.client import CClient
from hotel_room_manager.reservation import CReservation

from hotel_room_manager.room import CRoom

from .db_manager import CDbManager

from datetime import datetime

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
                      "Smoking allowed", "Next avaliable date", "Edit Room", "Delete Room")
    return render_template("all_rooms.html", data=all_rooms, headings=table_headings, view_redirect_page="/room-profile", delete_redirect_page="/delete-room")


@routes.route('/view-clients', methods=['POST', 'GET'])
def view_clients():
    all_clients = data_manager.get_all_clients()
    table_headings = ("ID", "Name", "Surname", "Birthday", "Adress", "CNP", "Email",
                      "Phone", "Edit Client", "Delete Client")
    return render_template("all_clients.html", data=all_clients, headings=table_headings, view_redirect_page="/client-profile", delete_redirect_page="/delete-client")


@routes.route('/view-reservations', methods=['POST', 'GET'])
def view_reservations():
    all_reservations = data_manager.get_all_reservations()
    table_headings = ["Reservation ID", "Room ID", "Room Number",
                      "Client ID", "Client Name", "Client Surname",
                      "Start Date", "End Date", "Parking", "Breakfast", "Dinner", "Total Price",
                      "Room Info", "Client Info", "Reservation Info", "Delete Reservation"]
    return render_template("all_reservations.html", data=all_reservations, headings=table_headings)


@routes.route('/client-profile/<client_id>', methods=['POST', 'GET'])
def view_client_profile(client_id):

    table_headings = ["Reservation ID", "Room Number", "Start Date",
                      "End Date", "View Reservation Details", "Delete Record"]

    if request.method == "POST":
        client_obj = CClient()
        client_obj.construct_from_form_data(request.form)
        data_manager.update_client(client_id, client_obj)

    client = data_manager.get_client_at_id(client_id)
    client_data = client.get_client_data()

    reservation_history = data_manager.get_client_reservation_history(
        client_id)

    return render_template("client_profile.html", client_data=client_data,
                           headings=table_headings, data=reservation_history, view_redirect_page='/reservation-profile', delete_redirect_page="/delete-reservation")


@routes.route('/reservation-profile/<reservation_id>', methods=['POST', 'GET'])
def view_reservation_profile(reservation_id):
    all_clients = data_manager.get_client_id_to_name()
    all_rooms = data_manager.get_room_id_to_number()

    if request.method == "POST":
        reservation_obj = CReservation()
        reservation_obj.construct_from_form_data(request.form)
        data_manager.update_reservation(reservation_id, reservation_obj)

    reservation = data_manager.get_reservation_at_id(reservation_id)
    reservation_data = reservation.get_reservation_data()
    selected_room = reservation_data['idroom']
    selected_client = reservation_data['idclient']

    return render_template("reservation-profile.html",
                           clients_combo_label_text="Clients", clients_combo_name="client_id", clients_combo_data=all_clients, clients_selected_option=selected_client,
                           rooms_combo_label_text="Rooms", rooms_combo_name="room_id", rooms_combo_data=all_rooms, rooms_selected_option=selected_room,
                           reservation_data=reservation_data)


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
    selected_floor = room_data['floor']
    selected_room_type = int(room_data['room_type'] or 0)

    return render_template("room_profile.html",
                           room_data=room.get_room_data(),
                           floor_combo_label_text="Floor", floor_combo_name='room_floor', floor_combo_data=floor_combo_data, floor_selected_option=selected_floor,
                           type_combo_label_text="Room Type", type_combo_name='room_type', type_combo_data=room_type_combo_data, type_selected_option=selected_room_type,
                           headings=table_headings, data=reservation_history, view_redirect_page='/reservation-profile', delete_redirect_page="/delete-reservation")


@routes.route('/delete-room/<room_id>', methods=['POST', 'GET'])
def delete_room(room_id):
    data_manager.delete_room(room_id)
    return redirect('/view-rooms')


@routes.route('/delete-client/<client_id>', methods=['POST', 'GET'])
def delete_client(client_id):
    data_manager.delete_client(client_id)
    return redirect('/view-clients')


@routes.route('/delete-reservation/<reservation_id>', methods=['POST', 'GET'])
def delete_reservation(reservation_id):
    data_manager.delete_reservation(reservation_id)
    return redirect('/view-reservations')


@routes.route('/add-client', methods=['POST', 'GET'])
def add_client():
    # Get client data from form
    client = CClient()
    client.construct_from_form_data(request.form)

    if request.method == "POST":
        data_manager.add_client(client)

    return render_template("insert_client.html")


@routes.route('/add-room', methods=['POST', 'GET'])
def add_room():
    # Get room data from form
    room = CRoom()
    room.construct_from_form_data(request.form)

    if request.method == "POST":
        data_manager.add_room(room)

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

    return render_template("insert_room.html",
                           floor_combo_label_text="Floor", floor_combo_name='room_floor', floor_combo_data=floor_combo_data, floor_selected_option=-1,
                           type_combo_label_text="Room Type", type_combo_name='room_type', type_combo_data=room_type_combo_data, type_selected_option=-1)


@routes.route('/make-reservation', methods=['POST', 'GET'])
def add_reservation():
    # Get reservation data from form
    reservation = CReservation()
    reservation.construct_from_form_data(request.form)

    all_clients = data_manager.get_client_id_to_name()
    all_rooms = data_manager.get_room_id_to_number()

    if request.method == "POST":
        data = request.form
        room_id = int(data.get('room_id') or 0)
        room = data_manager.get_room_at_id(room_id)
        # Set total price
        nb_days = (datetime.strptime(
            reservation._end_date, '%m/%d/%Y') - datetime.strptime(
                reservation._start_date, '%m/%d/%Y')).days
        total_price = nb_days * room._price
        reservation._total_price = total_price

        # Check if the starting date is avaliable for the selected room
        if room.check_avaliable_date(datetime.strptime(
                reservation._start_date, '%m/%d/%Y')) == True:
            data_manager.add_reservation(reservation)
            next_av_date = datetime.strptime(
                reservation._end_date, '%m/%d/%Y') + timedelta(days=1)
            data_manager.set_room_next_avaliable_date(
                room_id, next_av_date.date().strftime("%m/%d/%Y"))
        else:
            flash(
                'The start date you wanted is not avaliable! Please, choose another day', category='error')

    return render_template("make_reservation.html",
                           clients_combo_label_text="Clients", clients_combo_name="client_id", clients_combo_data=all_clients, clients_selected_option=-1,
                           rooms_combo_label_text="Rooms", rooms_combo_name="room_id", rooms_combo_data=all_rooms, rooms_selected_option=-1)
