"""

973. K Closest Points to Origin

Medium

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000


"""

from typing import List
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        kclosest = []
        kclosest.append((self.dist(points[0]), [points[0][0], points[0][1]]))

        for k in range(1, len(points)):
            if len(kclosest) < K:
                d = self.dist(points[k])
                kclosest.append((self.dist(points[k]), [points[k][0], points[k][1]]))
                heapq._siftup_max(kclosest, -1)

            elif abs(points[k][0]) < abs(kclosest[0][1][0]) and abs(points[k][1]) < abs(kclosest[0][1][1]):
                d = self.dist(points[k])
                heapq._heappop_max(kclosest)
                kclosest.append((self.dist(points[k]), [points[k][0], points[k][1]]))
                heapq._siftup_max(kclosest, -1)

            elif abs(points[k][0]) >= abs(kclosest[0][1][0]) and abs(points[k][1]) >= abs(kclosest[0][1][1]):
                continue

            else:
                d = self.dist(points[k])
                if d < kclosest[0][0]:
                    heapq._heappop_max(kclosest)
                    kclosest.append((self.dist(points[k]), [points[k][0], points[k][1]]))
                    heapq._siftup_max(kclosest, -1)

        res = []
        for p in kclosest:
            res.append(p[1])
        return res

    def dist(self, point):
        return sqrt(point[0]**2 + point[1]**2)


if __name__ == '__main__':
    sol = Solution()
    method = sol.kClosest

    cases = [

        # (method, ([[1,3],[-2,2]], 1), [[-2,2]]),
        (method, ([[-5,4],[-6,-5],[4,6]], 2), [[-5,4],[4,6]]),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i + 1, str(expected), str(ans)))