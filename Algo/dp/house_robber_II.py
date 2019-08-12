"""

213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums)==1:
            return nums[0]


        # only 3 possibilities: 1. include nums[0]; 2. include nums[-1]; 3. include neither

        dp0 = self.rob_helper(nums[0:-1])
        dp1 = self.rob_helper(nums[1:])
        dp2 = self.rob_helper(nums[1:-1])

        return max(dp0, dp1, dp2)

    def rob_helper(self, nums):
        """
        maximum sum without the circle formation

        :param nums: a list of positive integers
        :return: the maximum sum of a sub-sequence that does not contain 2 consecutive elements
        """

        if not nums:
            return 0

        if len(nums)==1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        max_dp = max(sum(nums[0:-1:2]), sum(nums[1::2]))

        for i in range(2, len(nums)):
            if i - 3 < 0:
                dp[i] = dp[i-2] + nums[i]
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
            max_dp = max(max_dp, dp[i])
        return max_dp


if __name__ == "__main__":

    sol = Solution()
    # nums = [2,1,1,2]              # 3
    # nums = [1,3,1,3,100]          # 103
    nums = [2,3,2]                # 3
    # nums = [2,7,9,3,1]            # 11
    # nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]         # 41
    # nums = [4,1,2,7,5,3,1]         # 14
    print(sol.rob(nums))