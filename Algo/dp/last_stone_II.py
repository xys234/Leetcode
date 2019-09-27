"""

1049
Medium

"""


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        n, total = len(stones), sum(stones)
        max_weight = 0
        dp = [0] * int(total // 2 + 1)
        dp[0] = True  # dp[i] indicates if there is a group of stones whose total weight is i

        for s in stones:

            # a reverse iteration guarantees that the larger weight will not used the smaller weight
            # produced by the current stone
            for j in range(total // 2, s - 1, -1):
                if dp[j - s]:
                    dp[j] = True
                    max_weight = max(max_weight, j)

        return (total - max_weight) - max_weight


if __name__ == '__main__':

        sol = Solution()
        method = sol.lastStoneWeightII

        cases = [

            (method, ([1,1,1],), 1),

        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if ans == expected:
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))