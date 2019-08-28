"""


There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.
When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.



Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.


"""

from typing import List
import heapq
from fractions import Fraction


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)

    def mincostToHireWorkers_faster(self, quality, wage, K):
        workers = sorted(zip(quality, wage), key=lambda x: x[1]/x[0])
        quality_heap = [-w[0] for w in workers[:K]]
        heapq.heapify(quality_heap)

        quality_sum = -sum(quality_heap)
        cost = quality_sum / workers[K-1][0] * workers[K-1][1]
        min_cost = cost

        for k in range(K, len(quality)):
            if workers[k][0] + quality_heap[0] < 0:
                quality_sum += heapq.heappushpop(quality_heap, -workers[k][0]) + workers[k][0]
                cost = quality_sum / workers[k][0] * workers[k][1]
                min_cost = min(cost, min_cost)
        return min_cost


if __name__ == '__main__':
    sol = Solution()
    method = sol.mincostToHireWorkers_faster

    cases = [
        # (method, ([10,20,5],[70,50,30],2), 105),
        (method, ([3,1,10,10,1],[4,8,2,2,7],3), 30.66667),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if abs(ans - expected) <= 1e-5:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))