import unittest
from laestrella import main

class TestMain(unittest.TestCase):

    def test_example(self):
        self.assertEqual(main.add(2, 3), 5)  # Método ejemplo que puedes personalizar

if __name__ == '__main__':
    unittest.main()