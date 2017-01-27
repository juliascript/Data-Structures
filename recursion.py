#!python

import unittest


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_iterative(n)


def factorial_iterative(n):
    # theta(1), O(n) 
    if type(n) == float:
        raise ValueError, 'function undefined for float'
    if n < 0:
        raise ValueError, 'function undefined for n < 0'
    elif n == 0:
        return 1
    elif n <= 2:
        return n
    else: 
        total = 1
        for i in range(int(n), 1, -1):
            total *= i
        return total
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests below


def factorial_recursive(n):
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)
