"""

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""



class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0]*len(s)     # dp[i] ~ the length of the valid parentheses at index i
        max_dp = 0
        for i in range(1, len(s)):
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = dp[i-2] + 2
            elif s[i] == ")" and s[i-1] == ")" and i-dp[i-1]-1>=0:
                if s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
            max_dp = max(max_dp, dp[i])
        return max_dp


if __name__ == "__main__":

    sol = Solution()
    # s = "(()"
    s = "(()())"
    # s = ")()())"
    print(sol.longestValidParentheses(s))