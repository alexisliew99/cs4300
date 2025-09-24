# Implement a Python using pytest to test case for each
# data type to ensure it matches the variable types of the correct value

from task2 import get_integer, get_float, get_string, get_boolean

def test_get_integer():
    assert get_integer() == 84

def test_get_float():
    assert get_float() == 8.992

def test_get_string():
    assert get_string() == "hello world"

def test_get_boolean():
    assert get_boolean() is True
