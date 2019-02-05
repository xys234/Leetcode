"""

96.

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1,i+1): # root node for i nodes
                dp[i] += dp[i-j] * dp[j-1]
        return dp[n]


if __name__=='__main__':

    sol = Solution()

    cases = [

        # (sol.numTrees, (3,), 5),
        (sol.numTrees, (1,), 1),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))