import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_standard(self):
        result = rectangle.area(12, 4)
        self.assertEqual(result, 48)

        result = rectangle.area(3, 15)
        self.assertEqual(result, 45)

        result = rectangle.area(100, 200)
        self.assertEqual(result, 20000)

    def test_area_zero_side(self):
        result = rectangle.area(10, 0)
        self.assertEqual(result, -1)

        result = rectangle.area(0, 1)
        self.assertEqual(result, -1)

    def test_area_negative_side(self):
        result = rectangle.area(-11, 12)
        self.assertEqual(result, -1)

        result = rectangle.area(112, -3)
        self.assertEqual(result, -1)

    def test_area_string(self):
        result = rectangle.area('abc', 12)
        self.assertEqual(result, -1)

        result = rectangle.area(12, 'abc')
        self.assertEqual(result, -1)

        result = rectangle.area('abc', 'def')
        self.assertEqual(result, -1)
        
        result = rectangle.area('101', 12)
        self.assertEqual(result, -1)

        result = rectangle.area(12, '101')
        self.assertEqual(result, -1)
        
        result = rectangle.area('101', '12')
        self.assertEqual(result, -1)

    def test_area_wrong_type(self):
        result = rectangle.area(None, 1)
        self.assertEqual(result, -1)

        result = rectangle.area(123, True)
        self.assertEqual(result, -1)

    def test_perimeter_standard(self):
        result = rectangle.perimeter(12, 4)
        self.assertEqual(result, 32)

        result = rectangle.perimeter(3, 15)
        self.assertEqual(result, 36)

        result = rectangle.perimeter(100, 200)
        self.assertEqual(result, 600)
       
    def test_perimeter_zero_side(self):
        result = rectangle.perimeter(10, 0)
        self.assertEqual(result, -1)

        result = rectangle.perimeter(0, 1)
        self.assertEqual(result, -1)

    def test_perimeter_negative_side(self):
        result = rectangle.perimeter(-11, 12)
        self.assertEqual(result, -1)

        result = rectangle.perimeter(112, -3)
        self.assertEqual(result, -1)

    def test_perimeter_string(self):
        result = rectangle.perimeter('abc', 12)
        self.assertEqual(result, -1)

        result = rectangle.perimeter(12, 'abc')
        self.assertEqual(result, -1)

        result = rectangle.perimeter('abc', 'def')
        self.assertEqual(result, -1)
        
        result = rectangle.perimeter('101', 12)
        self.assertEqual(result, -1)

        result = rectangle.perimeter(12, '101')
        self.assertEqual(result, -1)
        
        result = rectangle.perimeter('101', '12')
        self.assertEqual(result, -1)

    def test_perimeter_wrong_type(self):
        result = rectangle.perimeter(None, 1)
        self.assertEqual(result, -1)

        result = rectangle.perimeter(123, True)
        self.assertEqual(result, -1)
