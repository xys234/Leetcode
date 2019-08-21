"""

44. Wildcard Matching
Hard

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)

        dp = [[False] * (np + 1) for _ in range(ns + 1)]
        dp[0][0] = True

        for j in range(1, np + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]


if __name__ == "__main__":

    sol = Solution()
    method = sol.isMatch

    cases = [
        (method, ("aa","a"), False),
        (method, ("aa","*"), True),
        (method, ("cb","?a"), False),
        (method, ("adceb","*a*b"), True),
        (method, ("acdcb","a*c?b"), False),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))