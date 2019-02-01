"""

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile
has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either
the beginning or the end of the row.  This continues until there are no more piles left, at which point
the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.

"""

from functools import lru_cache
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        @lru_cache()
        def dp(i, j):
            if i > j:
                return 0
            turn = (j - i) % 2    # determine whose turn it is
            if turn == 1:
                return max(piles[i]+dp(i+1, j), piles[j]+dp(i, j-1))    # Alex's
            else:
                return min(-piles[i]+dp(i+1, j), -piles[j]+dp(i, j-1))   # Lee's turn; minimize his points

        return dp(0, len(piles)-1) > 0


if __name__=='__main__':

    sol = Solution()

    cases = [
        # (sol.find_pivot, ([3,4,5,6,7,1,2], 0, 6), 4),
        # (sol.find_pivot, ([1,2,3,4], 0, 3), -1),
        # (sol.find_pivot, ([1,3,5], 0, 2), 2),
        # (sol.findPivot, ([1,3,5], 0, 2), 2),
        # (sol.binary_search, ([1,2,3,4], 2, 0, 3), 1),
        # (sol.binary_search, ([1,2,3,4], 5, 0, 3), -1),
        # (sol.binary_search, ([1,2,3,4], 0, 0, 3), -1),
        # (sol.binary_search, ([1], 0, 0, 0), -1),
        # (sol.binary_search, ([1], 1, 0, 0), 0),
        (sol.stoneGame, ([5,3,4,6],), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
