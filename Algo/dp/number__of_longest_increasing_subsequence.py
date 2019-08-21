"""

673.
Medium


"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        lengths, counts = [1]*n, [1]*n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        ans = 0
        for length, count in zip(lengths, counts):
            if length == max_length:
                ans += count
        return ans


if __name__ == "__main__":

    sol = Solution()
    method = sol.findNumberOfLIS

    cases = [
        (method, ([1,3,5,4,7],), 2),
        (method, ([1,3,2],), 2),
        (method, ([1,2,3,1,2,3,1,2,3],), 10),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))