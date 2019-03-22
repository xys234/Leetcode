"""

698

Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


"""


class Solution:
    def canPartitionKSubsets(self, nums: 'list', k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False

        visited = [False for _ in nums]

        def dfs(curr_k, start_index, curr_sum, target):
            if curr_k == 0:
                return True
            if curr_sum == target:
                return dfs(curr_k-1, 0, 0, target)

            for i in range(start_index, len(nums)):
                if visited[i] or curr_sum + nums[i] > target:
                    continue
                visited[i] = True
                if dfs(curr_k, i+1, curr_sum+nums[i], target):
                    return True
                visited[i] = False
            return False

        return dfs(k, 0, 0, total / k)


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.canPartitionKSubsets, ([4, 3, 2, 3, 5, 2, 1], 4), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))