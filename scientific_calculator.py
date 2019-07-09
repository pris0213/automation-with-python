import math
from calculator import Calculator

class ScientificCalculator(Calculator):

    def power(self, first_number, second_number):
        return math.pow(first_number, second_number)

    def calc_circle_radius(self, radius):
        return math.pi * radius ** 2

    def get_pi(self):
        return math.pi

    