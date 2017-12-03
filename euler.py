#!/usr/bin/env python3
"""Project Euler."""

import unittest
import time
import itertools
import functools

def problem001(target=1000):
    """Add up all the multiples of 3 or 5."""
    return sum([i for i in range(1, target) if i % 3 == 0 or i % 5 == 0])

class TestProblem001(unittest.TestCase):
    """Problem #1 test cases."""
    def test_001testcase(self):
        """Check the answer to number 1's test case."""
        self.assertEqual(problem001(10), 23)

    def test_001answer(self):
        """Check the answer to number 1."""
        self.assertEqual(problem001(), 233168)

    def test_001time(self):
        """60 second check."""
        start = time.clock()
        problem001()
        finish = time.clock()
        self.assertGreater(start + 60, finish)

def fib(first, second):
    """Fibonacci sequence generator."""
    yield first
    yield second
    while True:
        first, second = second, first + second
        yield second

def problem002(target=4000000):
    """Return even Fibonacci numbers."""
    answer = [0]
    numbers = fib(0, 1)
    while answer[-1] < target:
        answer.append(numbers.__next__())
    answer.pop()
    return sum([i for i in answer if i % 2 == 0])

class TestProblem002(unittest.TestCase):
    """Test problem number two."""
    def test_002fib(self):
        """Make sure the Fibonacci generator is working."""
        self.assertEqual([i for i in itertools.islice(fib(1, 2), 10)],
                         [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    def test_002answer(self):
        """Check the answer to number two."""
        self.assertEqual(problem002(), 4613732)
    def test_002time(self):
        """60 second check."""
        start = time.clock()
        problem002()
        finish = time.clock()
        self.assertGreater(start + 60, finish)

def factors(i):
    """Find the factors of a number."""
    j = 2
    answer = []
    while i > 1:
        while i % j == 0:
            answer.append(j)
            i /= j
        j += 1
    return answer

def problem003(target=600851475143):
    """Problem number three."""
    return max(factors(target))

class TestProblem003(unittest.TestCase):
    """Check problem number three."""
    def test_003answer(self):
        """Confirm the correct answer."""
        self.assertEqual(problem003(), 6857)
    def test_003time(self):
        """60 second check."""
        start = time.clock()
        problem003()
        finish = time.clock()
        self.assertGreater(start + 60, finish)

def reverse(i):
    """Reverse a number."""
    return int(str(i)[::-1])

def is_palindrome(i):
    """See if a number matches the reverse of itself."""
    return i == reverse(i)

def problem004(target=3):
    """Problem number four."""
    return max([i * j for i in range(10 ** (target - 1), 10 ** target)
                for j in range(i, 10 ** target) if is_palindrome(i * j)])

class TestProblem004(unittest.TestCase):
    """Check problem number four."""
    def test_004test(self):
        """Check the test case."""
        self.assertEqual(problem004(2), 9009)
    def test_004answer(self):
        """Check the answer."""
        self.assertEqual(problem004(), 906609)
    def test_004time(self):
        """60 second check."""
        start = time.clock()
        problem004()
        finish = time.clock()
        self.assertGreater(start + 60, finish)

def gcd(first, second):
    """Greatest Common Denominator."""
    while first != second:
        if first < second:
            first, second = first, second - first
        if first > second:
            first, second = first - second, second
    return first

def lcm(first, second):
    """Least Common Multiple."""
    return first * second // gcd(first, second)

def problem005(target=20):
    """Problem number five."""
    return functools.reduce(lcm, range(1, target + 1))

class TestProblem005(unittest.TestCase):
    """Check problem number five."""
    def test_005test(self):
        """Check the test case."""
        self.assertEqual(problem005(10), 2520)
    def test_005answer(self):
        """Check the answer."""
        self.assertEqual(problem005(), 232792560)
    def test_005time(self):
        """60 second check."""
        start = time.clock()
        problem005()
        finish = time.clock()
        self.assertGreater(start + 60, finish)

def sumofsquares(numbers):
    return sum([i ** 2 for i in numbers])

def squareofsums(numbers):
    return sum(numbers) ** 2

def problem006(target=100):
    """Problem number six."""
    return squareofsums(range(1, target + 1)) - sumofsquares(range(1, target + 1))

class TestProblem006(unittest.TestCase):
    """Check problem number six."""
    def test_006test(self):
        """Check the test case."""
        self.assertEqual(problem006(10), 2640)
    def test_006answer(self):
        """Check the answer."""
        self.assertEqual(problem006(), 25164150)
    def test_006time(self):
        """60 second check."""
        start = time.clock()
        problem006()
        finish = time.clock()
        self.assertGreater(start + 60, finish)

if __name__ == "__main__":
    print(1, problem001())
    print(2, problem002())
    print(3, problem003())
    print(4, problem004())
    print(5, problem005())
    print(6, problem006())
