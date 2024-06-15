#!/usr/bin/python3
from typing import List
import math


def getPrimes(n : int) -> List[int]:
    """Returns two prime numbers that sum up to passed number"""
    # Start cases that are logical
    if n in [0, 1, 3]:
        return [-1, -1]

    # List prime numbers up till n as logic values of True and False
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Turn the list into numbers
    primes = []
    primes_set = set()
    for num in range(n + 1):
        if is_prime[num]:
            primes.append(num)
            primes_set.add(num)

    # Look for the happy couble
    for prime in primes:
        if (n - prime) in primes_set:
            return [prime, n - prime]

    return [-1, -1]


if __name__ == "__main__":
    print(getPrimes(10))
    print(getPrimes(100))
    print(getPrimes(3))
    print(getPrimes(72))
