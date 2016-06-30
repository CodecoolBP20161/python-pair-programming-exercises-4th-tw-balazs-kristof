class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        phone_number_1 = Person.normalize_phone_number(self._phone_number)
        phone_number_2 = Person.normalize_phone_number(input_phone_number)
        return phone_number_1[:len(phone_number_2)] == phone_number_2

    def get_name(self):
        return self._name

    @staticmethod
    def normalize_phone_number(phone_number):
        return phone_number.replace(" ", "").replace("-", "")
