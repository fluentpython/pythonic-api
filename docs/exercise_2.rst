=====================================
Exercise #2: Strategy without classes
=====================================


A. Review class-based implementation
------------------------------------

1. Go to ``exercises/vector`` directory

2. Run test for unary ``-`` with the ``-x`` option to stop at first error or failure:

.. code-block:: shell

    $ py.test -x test_vector_neg.py

3. Edit ``vector.py`` to implement a ``__neg__`` method for unary negation. That method should return a new ``Vector`` instance with each component negated. See ``test_vector_neg.py`` for the expected behavior.


C. Vector addition
------------------

1. Run tests for vector addition ``+`` with the ``-x`` option to stop at first error or failure:

.. code-block:: shell

    $ py.test -x test_vector_add.py

2. Edit ``vector.py`` to implement a ``__add__`` method for vector addition. That method should return a new ``Vector`` instance with each component of ``self`` added to the corresponding component of ``other``. See ``test_vector_add.py`` for the expected behaviors.
