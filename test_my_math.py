import my_math
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the math.py program
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = my_math.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = my_math.add(10.5, 2.0)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = my_math.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the math.py program
    """
    def test_subtract_integers(self):
        result = my_math.subtract(1, 1)
        self.assertEqual(result, 0)

    def test_subtract_floats(self):
        result = my_math.subtract(1.0, 0.5)
        self.assertEqual(result, 0.5)

    def test_subtract_strings(self):
        self.assertRaises(TypeError, my_math.subtract, ("xyz", "z"))

class TestMultiply(unittest.TestCase):
    """
    Test the multiplication function from the math.py program
    """
    def test_multiply_integers(self):
        result = my_math.multiply(1, 2)
        self.assertEqual(result, 2)

    def test_multiply_floats(self):
        result = my_math.multiply(2.0, 4.0)
        self.assertEqual(result, 8.0)

    def test_multiply_strings(self):
        self.assertRaises(TypeError, my_math.multiply, ('abc', 'def'))

class TestDivide(unittest.TestCase):
    """
    Test the divide function from the math.py program
    """
    def test_divide_integers(self):
        result = my_math.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide_floats(self):
        result = my_math.divide(30.0, 6.0)
        self.assertEqual(result, 5.0)

    def test_divide_strings(self):
        self.assertRaises(TypeError, my_math.divide, ('bbb', 'bbbbbb'))

if __name__ == '__main__':
    unittest.main()
