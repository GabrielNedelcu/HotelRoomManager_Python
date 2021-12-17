class CClient:
    _id_client = 0
    _name = ""
    _surname = ""
    _birthday = 0
    _adress = ""
    _cnp = 0
    _email = ""
    _phone = 0

    def __init__(self, name, surname, birthday, adress, cnp, email, phone):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self._adress = adress
        self._cnp = cnp
        self._email = email
        self._phone = phone

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
