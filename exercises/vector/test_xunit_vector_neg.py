import unittest

from vector import Vector

class TestStringMethods(unittest.TestCase):

    def test_vector_unary_minus(self):
        self.assertEqual(-Vector([1, 2, 3]), Vector([-1, -2, -3]))
