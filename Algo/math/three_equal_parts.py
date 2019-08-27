"""


"""

from typing import List


class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n, m = sum(A), len(A)
        if n % 3 != 0:
            return [-1, -1]

        target = n / 3
        target_trailing_zeros = 0
        first, third = -1, -1
        current_ones = 0
        for j in range(m-1, -1, -1):
            if A[j] == 1:
                current_ones += 1
                if current_ones == target:
                    third = j
                    break
            else:
                target_trailing_zeros += 1

        current_ones = 0
        current_trailing_zeros = 0
        for i in range(third-1):
            if A[i] == 1:
                current_ones += 1
                if current_ones == target:
                    first = i
                    break

        # fail to find the first partition
        if first < 0:
            return [-1, -1]
        i = first+1
        while current_trailing_zeros != target_trailing_zeros:
            if A[i] == 0:
                current_trailing_zeros += 1
                first += 1
            else:
                break

        # not enough trailing zeros
        if current_trailing_zeros != target_trailing_zeros:
            return [-1, -1]

        # find the middle partition
        current_ones = 0
        second = first + 1
        while second < third:
            if A[second] == 1:
                current_ones += 1
                if current_ones == target:
                    break
            second += 1

        if current_ones != target:
            return [-1, -1]

        current_trailing_zeros = 0
        while second < third:
            if A[second] == 0:
                current_trailing_zeros += 1
                if current_trailing_zeros == target_trailing_zeros:
                    break
            second += 1

        if current_trailing_zeros == target_trailing_zeros:
            return [first, second+1]


if __name__ == '__main__':
    sol = Solution()
    method = sol.threeEqualParts

    cases = [
        (method, ([1,0,1,0,1],), [0, 3]),
        # (method, ([1,1,0,1,1],), [-1, -1]),
        # (method, ([1,0,1,1,0],), [-1, -1]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))