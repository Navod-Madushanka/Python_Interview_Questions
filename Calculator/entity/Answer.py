class Answer:
    def __init__(self, answer=0.0):
        self._answer = answer

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value