"""

698.
Medium

Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, total = len(nums), sum(nums)
        if total % k != 0 or n < k:
            return False

        used = [False] * n

        def dfs(curr_grp, curr_sum, start, used, target, k):
            if curr_grp == k and curr_sum == target:
                return True
            elif curr_sum > target:
                return False
            elif curr_sum == target:
                return dfs(curr_grp+1, 0, 0, used, target, k)
            for i in range(start, n):
                if not used[i]:
                    used[i] = True
                    if dfs(curr_grp, curr_sum+nums[i], i+1, used, target, k):
                        return True
                    else:
                        used[i] = False
            return False

        return dfs(1, 0, 0, used, total // k, k)


if __name__ == '__main__':

    sol = Solution()
    method = sol.canPartitionKSubsets

    cases = [
        (method, ([4, 3, 2, 3, 5, 2, 1], 4), True),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))