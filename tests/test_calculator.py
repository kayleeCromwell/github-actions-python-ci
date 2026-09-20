import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
   def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-1, -1), -2)
    
    def test_subtract(self):
        # COMPLETE HERE
        self.assertEqual(sub(4, 2), 2)
        self.assertEqual(sub(6, 3), 3)
        self.assertEqual(sub(-2,-2), -4)


    def test_divide(self):
        # COMPLETE HERE
        self.assertEqual(div(12, 2), 6)
        self.assertEqual(div(12, 3), 4)
        self.assertEqual(div(8, 2), 4)
if __name__ == '__main__':

    unittest.main()
