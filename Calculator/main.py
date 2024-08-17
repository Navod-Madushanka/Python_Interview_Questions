from entity.FirstNumber import FirstNumber
from entity.Operator import Operator
from entity.SecondNumber import SecondNumber
from model.Calculation import Calculation


class Calculator:
    def __init__(self):
        self.first_number = FirstNumber()
        self.operator = Operator()
        self.second_number = SecondNumber()

    def get_user_data(self):
        try:
            self.first_number.first_number = float(input("Enter first number: "))
            self.operator.operator = input("Enter operator: ")
            self.second_number.number = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values for numbers.")

    def main(self):
        self.get_user_data()
        calculation = Calculation(self.first_number.first_number, self.operator.operator, self.second_number.number)
        answer = calculation.calculate_answer()
        print(answer.answer)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.main()
