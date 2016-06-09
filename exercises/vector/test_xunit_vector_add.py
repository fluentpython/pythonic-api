import unittest

from vector import Vector

class TestAddition(unittest.TestCase):


    def setUp(self):
        self.v2d = Vector([1, 2])
        

    def test_2d_vector_addition(self):
        v = Vector([3, 4]) + self.v2d
        self.assertEqual(v, Vector([4, 6]))


    def test_mismatched_lengths_exception(self):
        v = Vector([1, 2, 3])
        with self.assertRaises(ValueError):
            v + self.v2d


    def test_not_implemented_exception(self):
        with self.assertRaises(TypeError) as exc:
            self.v2d + 1
        assert 'unsupported operand' in str(exc.exception)
       

    def test_reversed_operator(self):
        v = [10, 20] + self.v2d
        self.assertEqual(v, Vector([11, 22]))
