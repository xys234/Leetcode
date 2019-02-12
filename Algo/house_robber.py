"""

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


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

        dp = [0] * len(nums)            # the gain including item nums[i]
        dp[0] = nums[0]
        dp[1] = nums[1]
        max_dp = max(sum(nums[0::2]), sum(nums[1::2]))

        for i in range(2, len(nums)):
            for j in range(0, i):
                if dp[i] < dp[j] + nums[i] and i-j >= 2:
                    dp[i] = dp[j] + nums[i]
                    if dp[i] > max_dp:
                        max_dp = dp[i]

        return max_dp



if __name__ == "__main__":

    sol = Solution()
    # nums = [2,1,1,2]
    # nums = [1,3,1,3,100]
    nums = [0]
    # nums = [2,7,9,3,1]
    print(sol.rob(nums))