import unittest
from ...models.base import Base
'''imports unittest module to provide a testing framework'''

class TestClassBase(unittest.TestCase):
    '''defines a class to begin testing'''
    def setUp(self):
        '''initializes resources needed for tests'''
        self.id = None

    def tearDown(self):
        '''method used for cleanup'''
        pass

    def test_id_default_value(id):
        '''method to check id default value'''
        obj = Base(None)
        self.assertIsNone(obj.id)

    def test_id_with_value(self):
        '''method to test value entered'''
        obj = Base(100)
        self.assertEqual(obj.id, 100)

    def test_incremented_id(self):
        '''method to test incrementation of id'''
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_pos_integer_id(self):
        '''method to check if id is > 0'''
        obj = Base(4)
        self.assertGreaterEqual(obj.id, 0)

if __name__ == "__main__"
    unittest.main()
