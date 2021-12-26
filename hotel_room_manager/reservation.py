
class CReservation:
    _id_reservation = 0
    _id_room = 0
    _id_client = 0
    _start_date = None
    _end_date = None
    _parking = False
    _breakfast = False
    _lunch = False
    _total_price = 0

    def __init__(self):
        self._id_reservation = 0
        self._id_room = 0
        self._id_client = 0
        self._start_date = None
        self._end_date = None
        self._parking = False
        self._breakfast = False
        self._lunch = False
        self._total_price = 0

    def construct_from_form_data(self, data):
        self._id_room = int(data.get('room_id') or 0)
        self._id_client = int(data.get('client_id') or 0)
        self._start_date = data.get('start_date')
        self._end_date = data.get('end_date')
        self._parking = True if data.get('parking_included') == 'on' else False
        self._breakfast = True if data.get(
            'breakfast_included') == 'on' else False
        self._lunch = True if data.get('lunch_included') == 'on' else False

    def construct_from_db_data(self, data):
        self._id_reservation = data[0][0]
        self._id_room = data[0][1]
        self._id_client = data[0][2]
        self._start_date = data[0][3]
        self._end_date = data[0][4]
        self._parking = data[0][5]
        self._breakfast = data[0][6]
        self._lunch = data[0][7]

    def get_reservation_data(self):
        data = {
            'idroom': self._id_room,
            'idclient': self._id_client,
            'start_date': self._start_date,
            'end_date': self._end_date,
            'parking': self._parking,
            'breakfast': self._breakfast,
            'dinner': self._lunch
        }

        return data

    def calculate_total_price(self):
        delta = self._end_date - self._start_date
        nb_days = delta.days
