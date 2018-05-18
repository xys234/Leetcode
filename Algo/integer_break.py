"""

343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and
maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.


"""

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n-1)
        dp[0] = 1

        for i in range(3, n+1):
            for j in range(1, i):
                if i-j < 2:
                    if j*(i-j) > dp[i-2]:
                        dp[i - 2] = j * (i-j)
                elif j*dp[i-j-2] > dp[i-2] or j*(i-j) > dp[i-2]:
                    dp[i-2] = j*max(dp[i-j-2], i-j)

        return dp[-1]

if __name__ == "__main__":

    sol = Solution()

    # case = 1
    # n = 10
    # ans = 36
    # if sol.integerBreak(n) == ans:
    #     print("Test case {0:d} passed".format(case))
    # else:
    #     print("Test case {0:d} FAILED".format(case))
    #
    # case = 2
    # n = 3
    # ans = 2
    # if sol.integerBreak(n) == ans:
    #     print("Test case {0:d} passed".format(case))
    # else:
    #     print("Test case {0:d} FAILED".format(case))
    #
    # case = 3
    # n = 2
    # ans = 1
    # if sol.integerBreak(n) == ans:
    #     print("Test case {0:d} passed".format(case))
    # else:
    #     print("Test case {0:d} FAILED".format(case))

    case = 4
    n = 4
    ans = 4
    if sol.integerBreak(n) == ans:
        print("Test case {0:d} passed".format(case))
    else:
        print("Test case {0:d} FAILED".format(case))