import math

class Calculator:

    def __init__(self, type):
        self.type = type

    def sum(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        if (second_number != 0):
            return first_number / second_number
        else:
            return "Error! You can\'t divide a number by zero."

    def power(self, first_number, second_number):
        return "Error! This operation is not available."