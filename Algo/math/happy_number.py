"""

202.
Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


"""


class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}
        while n != 1:
            if n in memo:
                return False
            memo[n] = 1
            n = self.sqr_sum(n)
        return True

    @staticmethod
    def sqr_sum(n):
        s = 0
        while n > 0:
            mod = n % 10
            s += mod**2
            n = n // 10
        return s


if __name__ == "__main__":
    sol = Solution()
    method = sol.isHappy

    cases = [
        (method, (19,), True),
        (method, (82,), True),
        (method, (34,), False),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))