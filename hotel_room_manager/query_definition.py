INSERT_ROOM_QUERY = ("INSERT INTO rooms"
                     "(room_number, floor, room_price, room_type, smoking)"
                     "VALUES (%(room_number)s, %(floor)s, %(room_price)s, %(room_type)s, %(smoking)s)")

INSERT_CLIENT_QUERY = ("INSERT INTO clients"
                       "(name, surname, birthday, adress, cnp, email, phone)"
                       "VALUES (%(name)s, %(surname)s, STR_TO_DATE(%(birthday)s,'%m/%d/%Y'), %(adress)s, %(cnp)s, %(email)s, %(phone)s)")

INSERT_RESERVATION_QUERY = ("INSERT INTO reservations"
                            "(idroom, idclient, start_date, end_date, parking, breakfast, dinner)"
                            "VALUES (%(idroom)s, %(idclient)s, STR_TO_DATE(%(start_date)s,'%m/%d/%Y'), STR_TO_DATE(%(end_date)s,'%m/%d/%Y'), %(parking)s, %(breakfast)s, %(dinner)s)")

GET_ALL_ROOMS = ("SELECT * FROM rooms")

GET_ALL_CLIENTS = ("SELECT * FROM clients")

GET_ALL_RESERVATIONS = ("SELECT * FROM reservations")

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
