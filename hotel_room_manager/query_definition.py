# FILE CONTAINING ALL THE QUERYS FOR THE DATABASE OPERATIONS
# DO NOT MODIFY!!


INSERT_ROOM_QUERY = ("INSERT INTO rooms"
                     "(room_number, floor, room_price, room_type, smoking)"
                     "VALUES (%(room_number)s, %(floor)s, %(room_price)s, %(room_type)s, %(smoking)s)")

INSERT_CLIENT_QUERY = ("INSERT INTO clients"
                       "(name, surname, birthday, adress, cnp, email, phone)"
                       "VALUES (%(name)s, %(surname)s, STR_TO_DATE(%(birthday)s,'%m/%d/%Y'), %(adress)s, %(cnp)s, %(email)s, %(phone)s)")

INSERT_RESERVATION_QUERY = ("INSERT INTO reservations"
                            "(idroom, idclient, start_date, end_date, parking, breakfast, dinner, total_price)"
                            "VALUES (%(idroom)s, %(idclient)s, STR_TO_DATE(%(start_date)s,'%m/%d/%Y'), STR_TO_DATE(%(end_date)s,'%m/%d/%Y'), %(parking)s, %(breakfast)s, %(dinner)s, %(total_price)s)")

GET_ALL_ROOMS = ("SELECT * FROM rooms")

GET_ALL_CLIENTS = ("SELECT * FROM clients")

GET_CLIENT_ID_TO_NAME = ("SELECT idclient, name, surname FROM clients")

GET_ROOM_ID_TO_NUMBER = ("SELECT idroom, room_number FROM rooms")

GET_ROOM_AT_ID = ("SELECT * FROM rooms WHERE idroom = '%s'")

GET_CLIENT_AT_ID = ("SELECT * FROM clients WHERE idclient = '%s'")

DELETE_ROOM = ("DELETE FROM rooms WHERE idroom = '%s'")

UPDATE_ROOM = ("UPDATE rooms "
               "SET room_number = '%s', floor = '%s', room_price = '%s', room_type = '%s', smoking ='%s'"
               "WHERE idroom = '%s'")

SELECT_RESERVATIONS_FOR_ROOM = ("SELECT "
                                "reservations.idreservation, clients.name, clients.surname, clients.phone, reservations.start_date, reservations.end_date "
                                "FROM reservations "
                                "INNER JOIN clients ON reservations.idclient = clients.idclient "
                                "WHERE idroom = '%s'")

SELECT_RESERVATIONS_FOR_CLIENT = ("SELECT "
                                  "reservations.idreservation, rooms.room_number, reservations.start_date, reservations.end_date "
                                  "FROM reservations "
                                  "INNER JOIN rooms ON reservations.idroom = rooms.idroom "
                                  "WHERE idclient = '%s'")

UPDATE_CLIENT = ("UPDATE clients "
                 "SET name = '%s', surname = '%s', birthday = STR_TO_DATE('%s', '%%m/%%d/%%Y'), adress = '%s', cnp ='%s', email = '%s', phone = '%s'"
                 "WHERE idclient = '%s'")

DELETE_CLIENT = ("DELETE FROM clients WHERE idclient = '%s'")

GET_ALL_RESERVATIONS = ("SELECT "
                        "reservations.idreservation, "
                        "reservations.idroom, rooms.room_number, "
                        "reservations.idclient, clients.name, clients.surname, "
                        "reservations.start_date, reservations.end_date, reservations.parking, reservations.breakfast, reservations.dinner, reservations.total_price "
                        "FROM reservations "
                        "INNER JOIN rooms ON reservations.idroom = rooms.idroom "
                        "INNER JOIN clients ON reservations.idclient = clients.idclient")

DELETE_RESERVATION = ("DELETE FROM reservations WHERE idreservation = '%s'")

GET_RESERVATION_AT_ID = (
    "SELECT * FROM reservations WHERE idreservation = '%s'")

UPDATE_RESERVATION = ("UPDATE reservations "
                      "SET idroom = '%s', idclient = '%s', start_date = STR_TO_DATE('%s','%%m/%%d/%%Y'), end_date = STR_TO_DATE('%s','%%m/%%d/%%Y'), parking = %s, breakfast = %s, dinner = %s "
                      "WHERE idreservation = '%s'")

SET_ROOM_NEXT_DATE = ("UPDATE rooms "
                      "SET next_avaliable_date = STR_TO_DATE('%s','%%m/%%d/%%Y') "
                      "WHERE idroom = '%s'")
