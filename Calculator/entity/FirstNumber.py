class FirstNumber:
    def __init__(self, first_number=0.0):
        self._first_number = first_number

    @property
    def first_number(self):
        return self._first_number

    @first_number.setter
    def first_number(self, value):
        self._first_number = value