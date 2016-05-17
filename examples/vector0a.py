'''
Vector: classe vetor euclideano

    >>> v1 = Vector([1, 2])
    >>> v1
    Vector([1.0, 2.0])
    >>> v1 * 10
    Vector([10.0, 20.0])
    >>> v1 * 'x'
    Traceback (most recent call last):
      ...
    TypeError: can't multiply sequence by non-int of type 'Vector'
    >>> 10 * v1
    Vector([10.0, 20.0])

'''

from array import array 
import math
import numbers

class Vector:

    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
    
    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __eq__(self, other):
        return (len(self) == len(other) and
            all(a == b for a, b in zip(self, other)))

    def __repr__(self):
        return 'Vector({})'.format(list(self))

    def __format__(self, format_spec):
        return repr(tuple(self))

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self) 
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

