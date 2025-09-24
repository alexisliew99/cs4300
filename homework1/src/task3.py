# Create a new file named task3.py. Create an if statement to check if a given number is positive,
# negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
# research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
# 1 to 100. 

# check if the number is positive/negative/zero
def check_numb(val):
    if val > 0:
        return "positive"
    elif val < 0:
        return "negative"
    else: 
        return "zero"

# returns a list of the first prime number
def first_primes(limit):
    primes = []
    num = 2
    
    while len(primes) < limit:
        is_prime = True
        
        # Check if num is prime
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
        
        # If no divisors found, it's prime
        if is_prime:
            primes.append(num)     
        num += 1 
    return primes

# calculates the sum of numbers from 1 to 100
def sum_to_100():
    total_result = 0
    numb = 1
    while numb <= 100:
        total_result += numb
        numb += 1
    return total_result
