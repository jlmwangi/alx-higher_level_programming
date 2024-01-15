import unittest
from ...models.square import Square


class TestClassSquare(unittest.TestCase):
    '''tests the square class inheriting from Rectangle'''
    def setUp(self):
        '''initializes resources needed to test the rectangle'''
        self.size = 10
        self.x = 7
        self.y = 10

    def tearDown(self):
        '''method used for cleanup'''
        pass

    def test_size_length(self):
        '''method to test value of size entered'''
        sq = Square(self.size, self.x, self.y)
        self.assertEqual(square.size, self.size)

    def test_x_greater_zero(self):
        '''tests x value is greater than zero'''
        sq = Square(self.size, self.x, self.y)
        self.assertGreater(square.x, 0)

    def test_y_greater_zero(self):
        '''tests value of y greater than zero'''
        sq = Square(self.size, self.x, self.y)
        self.assertGreater(square.y, 0)

    def test_area(self):
        '''tests that area is calculated correctly'''
        sq = Square(self.size, self.x, self.y)
        self.assertEqual(square.area(), self.size **2)

    def test_display(self):
        '''tests display method'''
        sq = Square(self.size, self.x, self.y)
        sq.display()

    def test_str_rep(self):
        '''tests string representation'''
        sq = Square(self.size, self.x, self.y)
        expected_str = f"[Square] ({square.id}) {square.x} / {square.y}\
                - {square.size}"
        self.assertEqual(str(square), expected_str)


    def test_args_order(self):
        '''check order of arguments'''
        correct_args = ["id", "size", "x", "y"]
        expected_args = ["id", "size", "x", "y"]
        for i, attr in enumerate(expected_args):
            self.assertEqual(attr, correct_args)

    def test_update_with_added_arguments(self):
        '''tests update using arguments added'''
        self.square.update(2, 3, 7, 9)
        self.assertEqual(self.square.size, 3)
        self.assertEqual(self.square.x, 7)
        self.assertEqual(self.square.y, 9)

    def test_update with args_skipping_kwargs(self):
        '''checks if args skips kwargs if args exists'''
        self.square.update(5, 7, 2, 1, size=3, x=5, y=2)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 1)
    
    __import__(square).__doc__

    __import__(square).Square.__doc__

    __import__(square).my_function.__doc__

    __import__(square).Square.my_function.__doc__


if __name__ = "__main__":
    unittest.main()
