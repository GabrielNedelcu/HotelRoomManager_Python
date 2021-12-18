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
    print(all_rooms)
    return render_template("all_rooms.html")


@routes.route('/view-clients')
def view_clients():
    return render_template("all_clients.html")


@routes.route('/view-reservations')
def view_reservations():
    return render_template("all_reservations.html")


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

    data_manager.add_reservation(reservation)
    return render_template("make_reservation.html")
