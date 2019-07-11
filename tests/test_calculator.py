import unittest

from scientific_calculator import ScientificCalculator
from calculator import Calculator
# import Calculator


class TestCalculator(unittest.TestCase):

    # Sum

    def test_sum_of_2_plus_1(self):
        first_number = 2
        second_number = 1
        calculator = Calculator("comum")

        self.assertEqual(3, calculator.sum(first_number, second_number))

    def test_sum_of_2_plus_negative_1(self):
        first_number = 2
        second_number = -1
        calculator = Calculator("comum")

        self.assertEqual(1, calculator.sum(first_number, second_number))

    # Subtract

    def test_subtraction_of_0_minus_1(self):
        first_number = 0
        second_number = 1
        calculator = Calculator("comum")

        self.assertEqual(-1, calculator.subtract(first_number, second_number))

    def test_subtraction_of_negative_2_minus_negative_4(self):
        first_number = -2
        second_number = -4
        calculator = Calculator("comum")

        self.assertEqual(2, calculator.subtract(first_number, second_number))

    # Multiply

    def test_multiplication_of_0_times_5(self):
        first_number = 0
        second_number = 5
        calculator = Calculator("comum")

        self.assertEqual(0, calculator.multiply(first_number, second_number))

    def test_multiplication_of_2_times_one_quarter(self):
        first_number = 2
        second_number = 0.25
        calculator = Calculator("comum")

        self.assertEqual(0.5, calculator.multiply(first_number, second_number))

    # Divide

    def test_division_of_2_by_0(self):
        first_number = 2
        second_number = 0
        calculator = Calculator("comum")

        self.assertEqual("Error! You can\'t divide a number by zero.",
                         calculator.divide(first_number, second_number))

    def test_division_of_2_by_one_quarter(self):
        first_number = 2
        second_number = 0.25
        calculator = Calculator("comum")

        self.assertEqual(8, calculator.divide(first_number, second_number))

    # Power

    def test_2_to_the_3rd_power(self):
        scientific_calculator = ScientificCalculator("CASSIO FX-350MS")

        first_number = 2
        second_number = 3

        self.assertEqual(8, scientific_calculator.power(first_number, second_number))

    def test_power_with_common_calculator(self):
        common_calculator = Calculator("Classe ED-205")

        first_number = 3
        second_number = 3

        self.assertEqual("Error! This operation is not available.",
                         common_calculator.power(first_number, second_number))
