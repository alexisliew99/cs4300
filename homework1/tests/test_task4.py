# Write pytest test cases to test the calculate_discount function with
# various types (integers, floats) for price and discount. 
import pytest
from task4 import calculate_discount

# test function call for int
def test_calculate_discount_integers():
    assert calculate_discount(100, 10) == 90

# test function call for float
def test_calculate_discount_floats():
    assert calculate_discount(200.0, 25.0) == 150.0

# Ensure proper exceptions are raised for incorrect input
def test_invalid_inputs():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
