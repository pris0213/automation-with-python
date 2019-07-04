import unittest
from hello_world import hello_world
import io
import sys

class test_hello_world(unittest.TestCase):
	def test_say(self):
		captured_output = io.StringIO()
		sys.stdout = captured_output
		hello_world.say()
		sys.stdout = sys.__stdout__

		expected = "Hello, World!\n"

		self.assertEqual(expected, 
						 captured_output.getvalue())


# Run tests
if __name__ == '__main__':
	unittest.main()