"""


"""

from math import sqrt


class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """

    def getFactors(self, n):

        def dfs(num, start):
            res = []
            for f in range(start, int(num)+1):
                if f ** 2 > num:
                    break
                if num % f == 0:
                    sub = dfs(num / f, f)
                    for s in sub:
                        res.append([int(f)]+s)
            res.append([int(num)])
            return res

        ans = dfs(n, 2)
        ans.pop()
        return ans


sol = Solution()
print(sol.getFactors(32))