"""

357.


"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for l in range(2, n+1):
            for i in range(1, n + 1):
                j = min(i + l-1, n)
                if j - i + 1 == l:
                    for k in range(i, j+1):
                        if k == i:
                            dp[i][j] = k + dp[i][k-1] + dp[k + 1][j]
                        else:
                            dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k + 1][j]))

        return dp[1][n]


if __name__ == "__main__":
    sol = Solution()
    method = sol.getMoneyAmount

    cases = [
        (method, (5,), 6),
        (method, (7,), 10),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i + 1, str(expected), str(ans)))