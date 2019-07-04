import unittest
from calculator import Calculator
# import Calculator

class test_Calculator(unittest.TestCase):

    # Sum

    def test_sum_of_2_plus_1(self):
        first_number = 2
        second_number = 1

        self.assertEqual(3, Calculator.sum(self, first_number, second_number))

    def test_sum_of_2_plus_negative_1(self):
        first_number = 2
        second_number = -1

        self.assertEqual(1, Calculator.sum(self, first_number, second_number))

    # Subtract

    def test_subtraction_of_0_minus_1(self):
        first_number = 0
        second_number = 1

        self.assertEqual(-1, Calculator.subtract(self, first_number, second_number))

    def test_subtraction_of_negative_2_minus_negative_4(self):
        first_number = -2
        second_number = -4

        self.assertEqual(2, Calculator.subtract(self, first_number, second_number))

    # Multiply

    def test_multiplication_of_0_times_5(self):
        first_number = 0
        second_number = 5

        self.assertEqual(0, Calculator.multiply(self, first_number, second_number))

    def test_multiplication_of_2_times_one_quarter(self):
        first_number = 2
        second_number = 0.25

        self.assertEqual(0.5, Calculator.multiply(self, first_number, second_number))

    # Divide

    def test_division_of_2_by_0(self):
        first_number = 2
        second_number = 0

        self.assertEqual("Error! You can\'t divide a number by zero.",
                         Calculator.divide(self, first_number, second_number))

    def test_division_of_2_by_one_quarter(self):
        first_number = 2
        second_number = 0.25

        self.assertEqual(8, Calculator.divide(self, first_number, second_number))

    # Power

    def test_2_to_the_3rd_power(self):
        scientific_calculator = Calculator("scientific")

        first_number = 2
        second_number = 3

        self.assertEqual(8, scientific_calculator.power(first_number, second_number))

    def test_power_with_common_calculator(self):
        common_calculator = Calculator("common")

        first_number = 3
        second_number = 3

        self.assertEqual("Error! This operation is not available.",
                         common_calculator.power(first_number, second_number))
