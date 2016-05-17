import pytest

from vector import Vector


@pytest.fixture
def v2d():
    return Vector([1, 2])


def test_2d_vector_addition(v2d):
    v = Vector([3, 4])
    assert v + v2d == Vector([4, 6])


def test_mismatched_lengths_exception(v2d):
    v = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        v + v2d


def test_not_implemented_exception(v2d):
    with pytest.raises(TypeError) as exc:
        v2d + 1
    assert 'unsupported operand' in str(exc.value)


def test_reversed_operator(v2d):
    assert [10, 20] + v2d == Vector([11, 22])
