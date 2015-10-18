"""
Library with functions for solving Project Euler problems.
"""

from sets import Set

def is_prime(num):
    """
    Determines whether a number is a prime
    """
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

def eratosthenes_sieve(top):
    """
    Eratosthenes sieve: after verifying that a number is a prime, mark all its
    factors as non primes.
    """

    not_primes = Set([])
    primes = []

    for num in range(2, top+1):
        if num not in not_primes and is_prime(num):
            primes.append(num)

            for i in range(2, top / num +1):
                not_primes.add(i*num)

    return primes
