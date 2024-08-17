class Operator:
    def __init__(self, operator=""):
        self._operator = operator

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
