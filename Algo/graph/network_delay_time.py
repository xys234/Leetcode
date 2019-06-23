"""

743

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node, and
w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
If it is impossible, return -1.

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.


"""

from heapq import *

INF = 1 << 60

class Solution:
    def networkDelayTime(self, times, N, K):
        d, q = [INF] * (N + 1), [(0, K)]
        d[K] = 0
        g = [[] for _ in range(N + 1)]
        for t in times:
            g[t[0]] += [(t[2], t[1])]
        while q:
            u = heappop(q)[1]
            for e in g[u]:
                t, v = d[u] + e[0], e[1]
                if t < d[v]:
                    d[v] = t
                    heappush(q, (d[v], v))
        return -(INF in d[1:]) or max(d[1:])


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.networkDelayTime, ([[2,1,1],[2,3,1],[3,4,1]],4,2), 2),
        (sol.networkDelayTime, ([[1,2,1],[2,3,2],[1,3,4]],3,1), 3),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))