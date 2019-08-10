"""

416.
Medium

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        target, n = int(s / 2), len(nums)
        dp = [[False]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[n][target]

    def canPartition_search(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2
        if max(nums) > target:
            return False
        nums.sort(reverse=True)
        return self.dfs(nums, target, 1)

    def dfs(self, nums, target, idx):
        if target == 0:
            return True
        elif target < 0:
            return False
        else:
            for i in range(idx, len(nums)):
                if self.dfs(nums, target - nums[i], i + 1):
                    return True
            return False


if __name__ == '__main__':

    sol = Solution()
    method = sol.canPartition

    cases = [
        (method, ([1, 5, 11, 5],), True),
        (method, ([1, 2, 3, 5],), False),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))