"""

354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than
the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

History:
2019.07.10

"""

from typing import List
import bisect


class Envelop:

    __slots__ = ('w', 'h')

    def __init__(self, e):
        self.w, self.h = e[0], e[1]

    def __lt__(self, other):
        if self.w < other.w:
            return True
        elif self.w == other.w:
            if self.h >= other.h:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return (self.w == other.w) and (self.h == other.h)

    def __repr__(self):
        return self.__class__.__name__ + f"({self.w}, {self.h})"


class Solution:
    def maxEnvelopes_TLE(self, envelopes: List[List[int]]) -> int:

        # O(n^2)
        envelopes = [Envelop(e) for e in envelopes]
        envelopes.sort()
        n = len(envelopes)

        if not n:
            return 0

        dp = [1 for _ in range(n)]
        max_count = 1
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if envelopes[i].w > envelopes[j].w and envelopes[i].h > envelopes[j].h:
                    dp[i] = max(dp[i], dp[j]+1)
                    max_count = max(max_count, dp[i])

        return max_count

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = [Envelop(e) for e in envelopes]
        envelopes.sort()
        n = len(envelopes)

        if n == 0:
            return 0
        seq = [envelopes[0].h]
        for i in range(1, n):
            h = envelopes[i].h
            k = bisect.bisect_left(seq, h)
            if k == len(seq):
                seq.append(h)
            else:
                seq.pop(k)
                seq.insert(k, h)
        return len(seq)

    def maxEnvelopes_solution(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = []
        res = 0

        for w, h in envelopes:
            ind = bisect.bisect_left(dp, h)
            if ind == len(dp):
                dp.append(h)
                res += 1
            else:
                dp[ind] = h
        return res


if __name__ == '__main__':

    sol = Solution()
    method = sol.maxEnvelopes

    cases = [
        (method, ([[5,4],[6,7],[6,4],[2,3]],), 3),
        (method, ([[4,5],[4,6],[6,7],[2,3],[1,1]],), 4),
        (method, ([[46,89],[50,53],[52,68],[72,45],[77,81]],), 3),
        (method, ([[10,8],[1,12],[6,15],[2,18]],), 2),
        (method, ([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]],), 5),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

    # envs = [[10,8],[1,12],[6,15],[2,18]]
    # envs = [Envelop(e) for e in envs]
    # envs.sort()
    #
    # k = bisect.bisect_left(envs, Envelop([3, 13]))
    # print(k)