"""

97. Interleaving string
Hard


"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n1+n2 != n3:
            return False

        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[0][0] = True

        for i in range(1, n1+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]

        for j in range(1, n2+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] != s3[i+j-1] and s2[j-1] != s3[i+j-1]:
                    dp[i][j] = False
                else:
                    first, second = False, False
                    if s1[i-1] == s3[i+j-1]:
                        first = dp[i-1][j]
                    if s2[j-1] == s3[i+j-1]:
                        second = dp[i][j-1]
                    dp[i][j] = first or second

        return dp[-1][-1]


if __name__ == "__main__":

    sol = Solution()
    method = sol.isInterleave

    cases = [
        (method, ("aabcc","dbbca","aadbbcbcac"), True),
        (method, ("aabcc","dbbca","aadbbbaccc"), False),
        (method, ("aabc","abad","aabadabc"), True),
        (method, ("db","b","cbb"), False),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i + 1, str(expected), str(ans)))


