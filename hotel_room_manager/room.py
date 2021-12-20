
class CRoom:
    _id_room = 0
    _number = 0
    _floor = 0
    _price = 0
    _type = 0
    _smoking = False

    def __init__(self):
        self._number = 0
        self._floor = 0
        self._price = 0
        self._type = 0
        self._smoking = False

    def construct_from_form_data(self, data):
        self._number = int(data.get('room_number') or 0)
        self._floor = int(data.get('room_floor') or 0)
        self._price = float(data.get('room_price') or 0)
        self._type = int(data.get('room_type') or 0)
        self._smoking = True if data.get('room_smoking') == 'on' else False

    def construct_from_db_data(self, data):
        self._id_room = data[0][0]
        self._number = data[0][1]
        self._floor = data[0][2]
        self._price = data[0][3]
        self._type = data[0][4]
        self._smoking = data[0][5]

    def get_room_data(self):
        data = {
            'room_number': self._number,
            'floor': self._floor,
            'room_price': self._price,
            'room_type': self._type,
            'smoking': self._smoking
        }

        return data
