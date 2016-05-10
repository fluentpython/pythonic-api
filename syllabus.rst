========
Syllabus
========

Title
    Pythonic APIs Workshop
    
Abstract
    Python is so consistent that often we can infer the behavior of new objects by assuming they work as the built-ins. The Python Data Model is the foundation of this consistent behavior. This workshop presents the construction of Pythonic objects: classes that feel "natural" to a Python programmer, and leverage some of the best language features by implementing key protocols of the Data Model.

Category
    Best Practices & Patterns 
    
Audience level
    Intermediate Python

Prerequisite knowledge
    Attendees should be very familiar with Python and know its key data structures and how to implement basic classes.
    
Materials or downloads needed in advance
    Attendees should have a laptop with Python 3.5 or newer installed. Although the content also applies to Python 2.7, 3.5 will be used in the examples.
    

Description
===========

This tutorial will show how to implement objects which behave as "naturally" as the built-in types, and therefore deserve to be called *Pythonic*. The whole presentation and exercises will be guided by doctests, which support a form of BDD (behavior-driven design) and allow participants to check their progress in the hands-on parts of the tutorial.

An API is considered Pythonic when it supports convenient and suitable Python idioms. For example, Python programmers expect that any collection is iterable and supports the ``len()`` function. Empty collections should evaluate "falsy" in boolean contexts. Objects of any type should have an user-friendly string representation, and another display format that doesn't hide details and is useful for debugging. Objects of several types support operators such as ``+`` and ``*`` when it makes sense. Pythonic objects are one of the keys to high programmer productivity with the language.

All of these object features, and more, are defined in the Python Data Model: the API that applies to Python objects in general, from plain integers to collections and even to functions and classes -- when we treat them as first class objects in the language. The most important of the special methods defined in the Data Model will be shown and exercised during the tutorial.


Outline
=======

Estimated time per topic in minutes (total: 180', including 15' coffee break)

* Introduction
    * (3') Tutorial Overview
* A simple but full-featured Pythonic class
    * (4') Object representation
    * (10') Exercise: Implement an Alternative Constructor
    * (7') Formatted Displays
    * (9') A Hashable Vector2d
    * (4') "Private" and “Protected” Attributes in Python
    * (5') The __slots__ Class Attribute: Use and Caveats
    * (9') Overriding Class Attributes
* A Pythonic Sequence
    * (7') The Sequence Interface
    * (15') Exercise: Implementing Sequence Behavior
* (15') -------------- Coffee Break --------------
* A Pythonic Sequence (continued)
    * (14') Slice-Aware __getitem__
    * (7') Dynamic Attribute Access
    * (10') Hashing and a Faster ==
    * (12') Exercise: Implement Formatting Support
* Operator Overloading Done Right
    * (5') Unary Operators
    * (10') Overloading + for Vector Addition
    * (7') Overloading * for Scalar Multiplication
    * (10') Exercise: Implement @ for Dot Product
    * (7') Rich Comparison Operators
    * (7') Augmented Assignment Operators
