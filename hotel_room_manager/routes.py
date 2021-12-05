from flask import Blueprint
from flask import render_template

routes = Blueprint('routes', __name__)

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

@routes.route('/add-room')
def add_room():
    return render_template("insert_room.html")

@routes.route('/make-reservation')
def add_reservation():
    return render_template("make_reservation.html")