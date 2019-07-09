import math
from calculator import Calculator

class ScientificCalculator(Calculator):

    def power(self, first_number, second_number):
        return math.pow(first_number, second_number)
