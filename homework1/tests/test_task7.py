# Implement pytest test cases
# to verify the correctness of your code when using the package

# Import numpy after downloadig it
from task7 import numpy_package
import numpy as np
import pytest

def test_numpy_package():
    arr, matrix = numpy_package()

    # Test 1D array
    expected_arr = np.array([1, 2, 3, 4, 5])
    assert np.array_equal(arr, expected_arr)

    # Test 2D array
    expected_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    assert np.array_equal(matrix, expected_matrix)
