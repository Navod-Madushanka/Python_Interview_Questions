from entity.Answer import Answer


class Calculation:
    def __init__(self, first_number, operator, second_number):
        self.first_number = first_number
        self.operator = operator
        self.second_number = second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number

    def modulo(self):
        return self.first_number % self.second_number

    def _calculate(self):
        if self.operator == "+":
            return self.addition()
        elif self.operator == "-":
            return self.subtraction()
        elif self.operator == "*":
            return self.multiplication()
        elif self.operator == "/":
            return self.division()
        elif self.operator == "%":
            return self.modulo()
        else:
            return 0

    def calculate_answer(self):
        answer = Answer()
        answer.answer = self._calculate()
        return answer
