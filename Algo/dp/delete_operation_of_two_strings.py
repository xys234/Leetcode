"""

583.
Medium

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.


"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + 1

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[-1][-1]


if __name__ == '__main__':

    sol = Solution()
    method = sol.minDistance

    cases = [
        (method, ("sea", "eat"), 2),
        (method, ("a", "b"), 2),
        (method, ("", "a"), 1),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))