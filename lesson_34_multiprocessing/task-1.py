# Task 1
# Primes
# NUMBERS = [
#    2,  # prime
#    1099726899285419,
#    1570341764013157,  # prime
#    1637027521802551,  # prime
#    1880450821379411,  # prime
#    1893530391196711,  # prime
#    2447109360961063,  # prime
#    3,  # prime
#    2772290760589219,  # prime
#    3033700317376073,  # prime
#    4350190374376723,
#    4350190491008389,  # prime
#    4350190491008390,
#    4350222956688319,
#    2447120421950803,
#    5,  # prime
# ]
# We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.
# Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.
# Compare the results and performance of each of them.

import time
from concurrent.futures import ThreadPoolExecutor
import math

NUMBERS = [
    2, 1099726899285419, 1570341764013157, 1637027521802551, 1880450821379411,
    1893530391196711, 2447109360961063, 3, 2772290760589219, 3033700317376073,
    4350190374376723, 4350190491008389, 4350190491008390, 4350222956688319,
    2447120421950803, 5
]


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def filter_primes(numbers):
    primes = []
    with ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
    for num, is_prime_result in zip(numbers, results):
        if is_prime_result:
            primes.append(num)
    return primes


res = filter_primes(NUMBERS)
print(f"Primes: {res}")
