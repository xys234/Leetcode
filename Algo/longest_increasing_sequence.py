"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums)            # length of the sequence
        tail = [0] * len(nums)          # number at the tail of the sequence
        tail[0] = nums[0]
        max_dp = dp[0]

        for i in range(1,len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    if dp[i] > max_dp:
                        max_dp = dp[i]

        return max_dp

if __name__ == "__main__":

    sol = Solution()
    # nums = [4,10,4,3,8,9]
    # nums = [10,22,9,33,21,50,41,60,80]
    # nums = [2, 2]
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.lengthOfLIS(nums))