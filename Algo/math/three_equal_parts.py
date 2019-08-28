"""


"""

from typing import List


class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n, m = sum(A), len(A)
        if n % 3 != 0:
            return [-1, -1]

        target_ones = int(n / 3)
        if target_ones == 0:
            return [0, m-1]

        target_trailing_zeros = 0
        for j in range(m - 1, -1, -1):
            if A[j] == 0:
                target_trailing_zeros += 1
            else:
                break

        def find_group(start, target_length=None):
            end = -1
            current_ones, current_trailing_zeros, first_one = 0, 0, -1
            for i in range(start, m):
                if A[i] == 1:
                    current_ones += 1
                    if current_ones == 1:
                        first_one = i
                else:
                    if current_ones == target_ones:
                        current_trailing_zeros += 1
                    else:
                        if target_length and current_ones >= 1 and i-first_one+1 > target_length:
                            return -1

                if current_ones == target_ones and current_trailing_zeros == target_trailing_zeros:
                    end = i
                    break
            return first_one, end

        def next_one(start):
            ind = -1
            for i in range(start, m):
                if A[i] == 1:
                    ind = i
                    break

            return ind

        first_one, first_end = find_group(0)
        second_one = next_one(first_end+1)
        second_end = second_one + (first_end - first_one + 1) - 1
        if A[first_one:first_end+1] != A[second_one:second_end+1]:
            return [-1, -1]

        third_one = next_one(second_end+1)
        if A[first_one:first_end+1] != A[third_one:]:
            return [-1, -1]

        return [first_end, second_end+1]


if __name__ == '__main__':
    sol = Solution()
    method = sol.threeEqualParts

    cases = [
        (method, ([1,0,1,0,1],), [0, 3]),
        (method, ([1,1,0,1,1],), [-1, -1]),
        (method, ([1,0,1,1,0],), [-1, -1]),
        (method, ([0,0,0,0,0],), [0, 4]),
        (method, ([0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0],), [-1, -1]),
        (method, ([1,0,1,0,1,0,1,1,1],), [-1, -1]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))