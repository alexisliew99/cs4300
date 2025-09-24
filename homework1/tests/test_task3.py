# Test to verify if it is correct for the code 
# for each control structure
from task3 import check_numb, first_primes, sum_to_100

def test_check_number():
    assert check_numb(5) == "positive"
    assert check_numb(-2) == "negative"
    assert check_numb(0) == "zero"

def test_first_primes():
    assert first_primes(5) == [2, 3, 5, 7, 11]

def test_sum_to_100():
    assert sum_to_100() == 5050
