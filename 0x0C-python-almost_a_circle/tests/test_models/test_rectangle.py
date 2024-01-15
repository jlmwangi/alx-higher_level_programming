import unittest
from ...models.rectangle import Rectangle


class TestClassRectangle(unittest.TestCase):
    '''defines a class to test a class rectangle'''
    def setUp(self):
        '''initializes resources needed to test the rectangle'''
        self.width = 10
        self.height = 5
        self.x = 7
        self.y = 10

    def tearDown(self):
        '''method used for cleanup'''
        pass

    def test_width_length(self):
        '''method to test value of width entered'''
        rect = Rectangle(self.width, self.height, self.x, self.y)
        self.assertEqual(rect.width, self.width)

    def test_x_greater_zero(self):
        '''tests x value is greater than zero'''
        rect = Rectangle(self.width, self.height, self.x, self.y)
        self.assertGreater(rect.x, 0)

    def test_y_greater_zero(self):
        '''tests value of y greater than zero'''
        rect = Rectangle(self.width, self.height, self.x, self.y)
        self.assertGreater(rect.y, 0)

    def test_height_greater_zero(self):
        '''tests that length is greater than zero'''
        rect = Rectangle(self.width, self.height, self.x, self.y)
        self.assertGreater(rect.height, 0)

    def test_width_greater_zero(self):
        '''tests width is greater than zero'''
        rect = Rectangle(self.width, self.height, self.x, self.y)
        self.assertGreater(rect.width, 0)

    def test_height_length(self):
        '''method to test value of height entered'''
        rect = Rectangle(self.width, self.height, self.x, self.y)
        self.assertEqual(rect.height, self.height)

    def test_x_length(self):
        '''tests value of x entered'''
        rect = Rectangle(self.width, self.height, x=14, self.y)
        self.assertEqual(rect.x, 14)

    def test_y_length(self):
        '''tests length of y entered'''
        rect = Rectangle(self.width, self.height, self.x, y=52)
        self.assertEqual(rect.y, 52)

    def test_invalid_types_width(self):
        '''tests for invalid type inserted'''
        with self.assertRaises(TypeError) as context:
            rect = Rectangle("width", self.height, self.x, self.y)
        error_message = "width must be an integer"
        self.assertEqual(str(context.exception), error_message)


    def test_invalid_values_width(self):
        '''tests invalid input values for the width'''
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(-6, self.height, self.x, self.y)
        error_message = "width must be > 0"
        self.assertEqual(str(context.exception), error_message)

    def test_invalid_types_height(self):
        '''tests invalid type for height'''
        with self.assertRaises(TypeError) as context:
            rect = Rectangle(self.width, True, self.x, self.y)
        error_message = "height must be an integer"
        self.assertEqual(str(context.exception), error_message)

    def test_invalid_values_height(self):
        '''tests negative value inputs for height'''
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(self.width, -1, self.x, self.y)
        error_message = "height must be > 0"
        self.assertEqual(str(context.exception), error_message)

    def test_invalid_type_x(self):
        '''tests for invalid types inserted'''
        with self.assertRaises(TypeError) as context:
            rect = Rectangle(self.width, self.height, "x", self.y)
        error_message = "x must be an integer"
        self.assertEqual(str(context.exception), error_message)

    def test_invalid_values_x(self):
        '''test negative value input for x'''
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(self.width, self.height, -7, self.y)
        error_message = "x must be >= 0"
        self.assertEqual(str(context.exception), error_message)

    def test_invalid_type_y(self):
        '''tests for invalid type y inserted'''
        with self.assertRaises(TypeError) as context:
            rect = Rectangle(self.width, self.height, self.x, 'c')
        error_message = "y must be an integer"
        self.assertEqual(str(context.exception), error_message)

    def test_invalid_values_y(self):
        '''tests for invalid inputs for y'''
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(self.width, self.height, self.x, -2)
        error_message = "y must be >= 0"
        self.assertEqual(str(context.exception), error_message)

    def test_area_calculation(self):
        '''tests the area calculation'''
        rect = rectangle(2, 7)
        expected_area = 2 * 7
        self.assertEqual(rect.area(), expected_area)

    def test_args_order(self):
        '''check if order is important'''
        correct_args = ["id", "width", "height", "x", "y"]
        expected_args = ["id", "width", "height", "x", "y"]
        for i, attr in enumerate(expected_args):
            self.assertEqual(attr, correct_args)

    def test_update_with_positional_arguments(self):
        '''tests update using positional arguments'''
        self.rectangle.update(2, 3, 4, 7 9)
        self.assertEqual(self.rectangle.width, 3)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 7)
        self.assertEqual(self.rectangle.y, 9)

    def test_update_with_mixed_arguments(self):
        '''tests update using missed arguments'''
        self.rectangle.update(5, height=5, y=4)
        self.assertEqual(self.rectangle.width, 3)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 7)
        self.assertEqual(self.rectangle.y, 4)

    def test_update_with_keyword_arguments(self):
        '''tests update using keyword arguments'''
        self.rectangle.update(width=4, height=5, x=6, y=7)
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 6)
        self.assertEqual(self.rectangle.y, 7)

    def test_update_with_no_args(self):
        '''check for no arguments'''
        self.rectangle.update()
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 6)
        self.assertEqual(self.rectangle.y, 7)

    def test_update with args_skipping_kwargs(self):
        '''checks if args skips kwargs if args exists'''
        self.rectangle.update(5, 7, 3, 2, 1, width=3, height=9, x=5, y=2)
        self.assertEqual(self.rectangle.width, 7)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 1)

    __import__(rectangle).__doc__

    __import__(rectangle).Rectangle.__doc__

    __import__(rectangle).my_function.__doc__

    __import__(rectangle).Rectangle.my_function.__doc__

if __name__ == "__main__"
    unittest.main()
