"""



"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n + 1)]
        dp[1] = [1] * n

        for k in range(2, n + 1):
            for i in range(k - 1, n):
                for j in range(k - 2, i):
                    if nums[i] > nums[j]:
                        dp[k][i] += dp[k - 1][j]

        max_length = 1
        for k in range(n, 1, -1):
            if max(dp[k]) > 0:
                max_length = k
                break
        return max(dp[max_length])


if __name__ == "__main__":

    sol = Solution()
    method = sol.findNumberOfLIS

    cases = [
        (method, ([1,3,5,4,7],), 2),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))