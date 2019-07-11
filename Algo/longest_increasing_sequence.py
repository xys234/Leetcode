"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

History:
2018.06.09
2019.07.10

"""

import bisect


class Solution:
    def lengthOfLIS_dp(self, nums):
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

    def lengthOfLIS(self, nums):
        # DP with binary search

        n = len(nums)
        if n == 0:
            return 0

        seq = [nums[0]]
        for i in range(1, n):
            if nums[i] > seq[-1]:
                seq.append(nums[i])
            else:
                k = bisect.bisect_left(seq, nums[i])
                seq.pop(k)
                seq.insert(k, nums[i])
        return len(seq)


if __name__ == "__main__":

    sol = Solution()
    method = sol.lengthOfLIS

    cases = [
        # (method, ([[5,4],[6,7],[6,4],[2,3]],), 3),
        # (method, ([[4,5],[4,6],[6,7],[2,3],[1,1]],), 4),
        # (method, ([[46,89],[50,53],[52,68],[72,45],[77,81]],), 3),
        (method, ([10, 9, 2, 5, 3, 7, 101, 18],), 4),
        # (method, ([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]],), 5),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
