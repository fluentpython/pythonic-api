from vector import Vector

def test_vector_unary_minus():
    assert -Vector([1, 2, 3]) == Vector([-1, -2, -3])
