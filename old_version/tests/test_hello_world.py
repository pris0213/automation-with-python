import unittest
from old_version.hello_world import HelloWorld
import io
import sys

class test_hello_world(unittest.TestCase):
	def test_say(self):
		captured_output = io.StringIO()
		sys.stdout = captured_output
		HelloWorld.say()
		sys.stdout = sys.__stdout__

		expected = "Hello, World!\n"

		self.assertEqual(expected, 
						 captured_output.getvalue())


# Run tests
if __name__ == '__main__':
	unittest.main()