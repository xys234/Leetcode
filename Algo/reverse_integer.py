"""

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:.
For the purpose of this problem, assume that your function returns 0 [-2**31, 2**31-1]
when the reversed integer overflows.


"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        sign = 1
        if x < 0:
            sign = -1

        num_str = str(abs(x))
        num = 0
        if num_str[-1] == '0':
            num = sign * int(num_str[:-1][::-1])
        num = sign * int(num_str[::-1])
        if num < -2 ** 31 or num > 2 ** 31 - 1:
            return 0
        else:
            return num


