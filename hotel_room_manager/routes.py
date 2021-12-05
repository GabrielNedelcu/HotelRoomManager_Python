from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/view-rooms')
def view_rooms():
    return render_template("all_rooms.html")

@views.route('/view-clients')
def view_clients():
    return render_template("all_clients.html")

@views.route('/view-reservations')
def view_reservations():
    return render_template("all_reservations.html")

@views.route('/client-profile')
def view_client_profile():
    return render_template("client_profile.html")

@views.route('/room-profile')
def view_room_profile():
    return render_template("room_profile.html")

@views.route('/add-client')
def add_client():
    return render_template("insert_client.html")

@views.route('/add-room')
def add_room():
    return render_template("insert_room.html")

@views.route('/make-reservation')
def add_reservation():
    return render_template("make_reservation.html")