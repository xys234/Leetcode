"""

1000.
Hard


There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile,
and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


"""

from typing import List
from functools import lru_cache

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n-1) % (K-1) != 0:
            return -1
        MAX_COST = 10000

        # dp[i][j][k] is the min. cost for merging pile i to pile j into k piles
        dp = [[[MAX_COST] * (K+1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = 0

        sums = [0 for _ in range(n)]
        sums[0] = stones[0]
        for j in range(1, n):
            sums[j] = sums[j-1]+stones[j]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(2, K + 1):
                    # split point. left sequence into 1 pile. right into k-1 pile
                    if l >= k:
                        for m in range(i, j):
                            dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k - 1])

                if dp[i][j][K] < MAX_COST:
                    dp[i][j][1] = dp[i][j][K] + sums[j] - sums[i] + stones[i]

        return dp[0][n - 1][1]


    def mergeStones_optimized(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1

        prefix = [0] * (n + 1)
        for i in range(n): prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j):  # cost to merge [i, j]
            if j - i + 1 < K: return 0

            ret = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))

            if (j - i) % (K - 1) == 0: ret += prefix[j + 1] - prefix[i]

            return ret

        return dp(0, n - 1)

if __name__ == '__main__':

    sol = Solution()
    method = sol.mergeStones

    cases = [
        (method, ([3,2,4,1],2), 20),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))