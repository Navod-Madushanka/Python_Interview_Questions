class SecondNumber:
    def __init__(self, number=0.0):
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
