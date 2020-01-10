"""

1278.
Hard


You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
Return the minimal number of characters that you need to change to divide the string.



Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0


"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        def palindrome_cost(s):
            cost = [[0 for _ in s] for _ in s]
            n = len(s)
            for i in range(n-1):
                cost[i][i+1] = int(s[i] != s[i+1])

            for l in range(3, n+1):
                for i in range(n-l+1):
                    cost[i][i+l-1] = cost[i+1][i+l-2] + int(s[i] != s[i+l-1])
            return cost

        cost = palindrome_cost(s)
        n = len(s)

        if n == k:
            return 0

        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = cost[0][i-1]     # first i elements into 1 group

        for k in range(2, k + 1):
            for i in range(k, n + 1):
                for j in range(1, i):
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + cost[j][i-1])
        return dp[-1][-1]


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.palindromePartition, ("abc", 2), 1),
        (sol.palindromePartition, ("aabbc",3), 0),
        (sol.palindromePartition, ("leetcode",8), 0),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))