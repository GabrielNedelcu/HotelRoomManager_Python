
class CRoom:
    _id_room = 0
    _number = 0
    _floor = 0
    _price = 0
    _type = 0
    _smoking = False

    def __init__(self, number, floor, price, type, smoking):
        self._number = int(number or 0)
        self._floor = int(floor or 0)
        self._price = float(price or 0)
        self._type = int(type or 0)
        self._smoking = True if smoking == 'on' else False

    def get_room_data(self):
        data = {
            'room_number': self._number,
            'floor': self._floor,
            'room_price': self._price,
            'room_type': self._type,
            'smoking': self._smoking
        }

        return data
