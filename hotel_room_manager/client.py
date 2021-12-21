class CClient:
    _id_client = 0
    _name = ""
    _surname = ""
    _birthday = 0
    _adress = ""
    _cnp = 0
    _email = ""
    _phone = 0

    def __init__(self):
        self._name = 0
        self._surname = 0
        self._birthday = 0
        self._adress = 0
        self._cnp = 0
        self._email = 0
        self._phone = 0

    def construct_from_form_data(self, data):
        self._name = data.get('client_name')
        self._surname = data.get('client_surname')
        self._birthday = data.get('client_birthday')
        self._adress = data.get('client_adress')
        self._cnp = data.get('client_cnp')
        self._email = data.get('client_email')
        self._phone = data.get('client_phone')

    def construct_from_db_data(self, data):
        self._id_client = data[0][0]
        self._name = data[0][1]
        self._surname = data[0][2]
        self._birthday = data[0][3]
        self._adress = data[0][4]
        self._cnp = data[0][5]
        self._email = data[0][6]
        self._phone = data[0][7]

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
