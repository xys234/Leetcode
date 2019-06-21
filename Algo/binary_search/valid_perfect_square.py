"""

367.

Easy

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num
        while l < r:
            m = l + (r - l) // 2
            sqr = m ** 2
            if abs(sqr - num) < 1e-6:
                return True
            elif sqr < num:
                l = m + 1
            else:
                r = m
        return False


if __name__ == '__main__':
    sol = Solution()
    method = sol.isPerfectSquare

    cases = [
        # (method, (16,), True),
        (method, (14,), False),
        (method, (1,), True),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
