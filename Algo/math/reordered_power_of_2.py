"""

869. Reordered Power of 2

Starting with a positive integer N, we reorder the digits in any order (including the original order)
such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true


Note:

1 <= N <= 10^9


"""

from math import log2, ceil, floor, pow
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        num_str = str(N)
        n = len(num_str)
        powers = self.findpowers(n)
        candidate_digit_counts = [self.count_digits(x) for x in powers]
        target_digit_count = Counter(num_str)
        return target_digit_count in candidate_digit_counts

    def findpowers(self, n):
        '''

        find all n-digit powers of 2
        :param n:
        :return:

        '''

        lb, hb = int('1'+'0'*(n-1)), int('9'*n)
        lb, hb = ceil(log2(lb)), floor((log2(hb)))
        return [str(int(pow(2, p))) for p in range(lb, hb+1)]

    @staticmethod
    def count_digits(num):
        """
        Count the occurrences of each digit of an integer string
        :param num: a string
        :return:
        """

        return Counter(num)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findpowers(3))
    # print(sol.count_digits('821'))
    # print(sol.count_digits('821') == Counter({'8': 1, '1': 1, '2': 1}))

    method = sol.reorderedPowerOf2

    cases = [
        (method, (24,), False),
        (method, (46,), True),
        (method, (16,), True),
        (method, (128,), True),
        (method, (821,), True),
        (method, (7235,), False),
        (method, (7236,), False),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

