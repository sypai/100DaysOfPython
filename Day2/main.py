# Python Data Types
"""Whenever needed, go through this: https://realpython.com/python-data-types/"""

# Python Operators and Expressions
"""https://realpython.com/python-operators-expressions/"""

# Big integers can be written using _ in between them.
print(421_155_233)

# String Formatting
# % - formatting
name = "Suyash"
print("Hello, %s" % name)

# str.format
age = 24
print("Hello, {}. You are {}".format(name, age))

# f - strings
# These are evaluated at run-time, we can put all valid python
# expressions
print(f'Hello, {name}. You are {age}')