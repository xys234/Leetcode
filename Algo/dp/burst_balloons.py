"""

312.
Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get
nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


"""

from typing import List


class Solution:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        padded = [1]*(n+2)
        padded[1:-1] = nums

        dp = [[0]*(n+2) for _ in range(n+2)]

        # for substring, update dp array by substring length and starting point
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1]+dp[k+1][j]+padded[i-1]*padded[k]*padded[j+1])
        return dp[1][n]


if __name__ == '__main__':

    sol = Solution()
    method = sol.maxCoins

    cases = [
        (method, ([3,1,5,8],), 167),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))