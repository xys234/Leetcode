class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        dp[0][0] = 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]
                    if dp[i - 1][j] > dp[i][j]:
                        dp[i][j] = dp[i - 1][j]

        i, j = n1, n2
        ans = []

        while i > 0 or j > 0:
            if i >= 1 and j >= 1 and str1[i-1] == str2[j-1]:
                ans.append(str1[i-1])
                i -= 1
                j -= 1
            elif i >= 1 and dp[i-1][j] == dp[i][j]:
                ans.append(str1[i-1])
                i -= 1
            elif j >= 1 and dp[i][j-1] == dp[i][j]:
                ans.append(str2[j-1])
                j -= 1
            elif i == 0 and j > 0:
                ans.append(str2[j-1])
                j -= 1
            elif i > 0 and j == 0:
                ans.append(str1[i-1])
                i -= 1
        return ''.join(reversed(ans))


sol = Solution()
# print(sol.shortestCommonSupersequence("abac", "cab"))
# print(sol.shortestCommonSupersequence("bbbaaaba", "bbababbb"))
# print(sol.shortestCommonSupersequence("bbabacaa", "cccababab"))
print(sol.shortestCommonSupersequence("ababaabbbb", "cbcbacaab"))