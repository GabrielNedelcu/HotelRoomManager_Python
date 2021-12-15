from flask import Blueprint
from flask import render_template
from flask import request

from hotel_room_manager.room import CRoom

from .db_manager import CDbManager

routes = Blueprint('routes', __name__)

data_manager = CDbManager()


@routes.route('/')
@routes.route('/home')
def home():
    return render_template("home.html")


@routes.route('/view-rooms')
def view_rooms():
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


@routes.route('/add-client')
def add_client():
    return render_template("insert_client.html")


@routes.route('/add-room', methods=['GET', 'POST'])
def add_room():
    # Get room data from form
    room_number = request.form.get('room_number')
    room_price = request.form.get('room_price')
    room_floor = request.form.get('room_floor')
    room_type = request.form.get('room_type')
    room_smoking = request.form.get('room_smoking')

    room = CRoom(room_number, room_floor,
                 room_price, room_type, room_smoking)

    # data_manager.check_connection()
    # print(room.get_room_data())
    data_manager.add_room(room)
    return render_template("insert_room.html")


@routes.route('/make-reservation')
def add_reservation():
    return render_template("make_reservation.html")
