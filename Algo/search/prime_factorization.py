"""

Lintcode 235.
Easy

Prime factorize a given integer.

Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]
Notice
You should sort the factors in ascending order.

"""

from math import sqrt


class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        ub = int(sqrt(num)) + 1
        factors = []

        def dfs(n, curr):
            if self.is_prime(n):
                factors.extend(curr + [n])
                return

            ub = int(sqrt(n)) + 1
            for i in range(2, ub):
                if n % i == 0:
                    dfs(n // i, curr + [i])
                    break

        dfs(num, [])
        return factors

    @staticmethod
    def is_prime(num):
        ub = int(sqrt(num)) + 1

        if num == 2:
            return True

        if num > 2 and num % 2 == 0:
            return False

        for i in range(3, ub, 2):
            if num % i == 0:
                return False

        return True