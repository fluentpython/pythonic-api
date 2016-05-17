==================
Pythonic APIs
==================

Consistency
------------

Python::

    len(text)  # string
    len(rate)  # array of floats
    len(names)  # list

Java:

.. code-block:: Java

    texto.length()  // String
    pesos.length    // array of floats
    nomes.size()    // ArrayList


``vector_v0.py``
----------------

Importing::

    >>> from examples.vector_v0 import Vector

Tests with 2 dimensions::

    >>> v1 = Vector([3, 4])
    >>> len(v1)
    2
    >>> abs(v1)
    5.0
    >>> v1 == Vector((3.0, 4.0))
    True
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> list(v1)
    [3.0, 4.0]

Tests with 3 dimensions::

    >>> v1 = Vector([3, 4, 5])
    >>> x, y, z = v1
    >>> x, y, z
    (3.0, 4.0, 5.0)
    >>> abs(v1)  # doctest:+ELLIPSIS
    7.071067811...


Tests with more dimensions::

    >>> v7 = Vector(range(7))
    >>> tuple(v7)
    (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    >>> abs(v7)  # doctest:+ELLIPSIS
    9.53939201...



.. literalinclude:: ../examples/vector_v0.py


``vector_v1.py``
----------------


Importing::

    >>> from examples.vector_v1 import Vector


Vector representations::

    >>> Vector([3.1, 4.2])
    Vector([3.1, 4.2])
    >>> Vector(range(10))
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    >>> v3 = Vector([3, 4, 5])
    >>> v3
    Vector([3.0, 4.0, 5.0])
    >>> v3_clone = eval(repr(v3))
    >>> v3_clone == v3
    True
    >>> print(v3_clone)
    (3.0, 4.0, 5.0)


.. literalinclude:: ../examples/vector_v1.py


``vector_v2.py``
----------------

Importing::

    >>> from examples.vector_v2 import Vector


Emulating sequences::

    >>> v = Vector([10, 20, 30, 40, 50])
    >>> v[0]
    10.0
    >>> v[-1]
    50.0
    >>> v[:3]
    Vector([10.0, 20.0, 30.0])


.. literalinclude:: ../examples/vector_v2.py


``vector_v3.py``
----------------

Importing::

    >>> from examples.vector_v3 import Vector


Basic tests of operator ``*``::

    >>> v1 = Vector([1, 2, 3])
    >>> v1 * 10
    Vector([10.0, 20.0, 30.0])


Tests of ``*`` with unusual but valid operands::

    >>> v1 * True
    Vector([1.0, 2.0, 3.0])
    >>> from fractions import Fraction
    >>> v1 * Fraction(1, 3)  # doctest:+ELLIPSIS
    Vector([0.3333..., 0.6666..., 1.0])

This version has a problem::


    >>> 10 * v1
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'Vector'


.. literalinclude:: ../examples/vector_v3.py



In Python, you can compute compound interest using a formula written like this::

    interest = principal * ((1 + rate) ** periods - 1)

The Python formula works with any numeric type that overloads the arithmetic operators.

In Java, only the primitive types support the arithmentic operators. If a financial app needs to use BigDecimal for enhanced precision, the compound interest formula has to be coded with method calls, like this:

.. code-block:: Java

    interest = principal.multiply(BigDecimal.ONE.add(rate).pow(periods).subtract(BigDecimal.ONE));


.. literalinclude:: ../examples/vector_v3.py


``vector_v4.py``
----------------

Importing::

    >>> from examples.vector_v4 import Vector


The reversed operator::

    >>> v1 = Vector([1, 2, 3])
    >>> 10 * v1
    Vector([10.0, 20.0, 30.0])


.. literalinclude:: ../examples/vector_v4.py


``vector_v5.py``
----------------

Importing::

    >>> from examples.vector_v5 import Vector

Tests for operator `@` (Python >= 3.5), computing the dot product::

    >>> va = Vector([1, 2, 3])
    >>> vz = Vector([5, 6, 7])
    >>> va @ vz == 38.0  # 1*5 + 2*6 + 3*7
    True
    >>> [10, 20, 30] @ vz
    380.0
    >>> va @ 3
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for @: 'Vector' and 'int'

.. literalinclude:: ../examples/vector_v5.py


``vector_v6.py``
----------------

Importing::

    >>> from examples.vector_v6 import Vector

Tests of hashing::

    >>> v1 = Vector([3, 4])
    >>> hash(v1) == 3 ^ 4
    True
    >>> v3 = Vector([3, 4, 5])
    >>> hash(v3) == 3 ^ 4 ^ 5
    True
    >>> v6 = Vector(range(6))
    >>> hash(v6) == 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5
    True
    >>> v2 = Vector([3.1, 4.2])
    >>> hash(v2) == hash(3.1) ^ hash(4.2)
    True
    >>> {v1, v2, v3, v6}
    {Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...]), Vector([3.0, 4.0, 5.0]), Vector([3.0, 4.0]), Vector([3.1, 4.2])}
 
Most hash values of non-integers vary from a 32-bit to 64-bit CPython build::

    >>> import sys
    >>> hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)
    True


.. literalinclude:: ../examples/vector_v6.py
