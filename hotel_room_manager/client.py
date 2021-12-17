class CClient:
    _id_client = 0
    _name = ""
    _surname = ""
    _birthday = 0
    _adress = ""
    _cnp = 0
    _email = ""
    _phone = 0

    def __init__(self, data):
        self._name = data.get('client_name')
        self._surname = data.get('client_surname')
        self._birthday = data.get('client_birthday')
        self._adress = data.get('client_adress')
        self._cnp = data.get('client_cnp')
        self._email = data.get('client_email')
        self._phone = data.get('client_phone')

    def get_client_data(self):
        data = {
            'name': self._name,
            'surname': self._surname,
            'birthday': self._birthday,
            'adress': self._adress,
            'cnp': self._cnp,
            'email': self._email,
            'phone': self._phone
        }

        return data
