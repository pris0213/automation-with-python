import unittest
import math_functions
import math

class known_values(unittest.TestCase):
	def test_area_circle_for_10_radius(self):
		result = math_functions.area_circle(10)

		expected = math.pi * 10 ** 2
		self.assertEqual(expected, result)

	def test_area_circle_for_2_radius(self):
		result = math_functions.area_circle(2)

		expected = math.pi * 2 ** 2
		self.assertEqual(expected, result)

# Run tests
if __name__ == '__main__':
	unittest.main()