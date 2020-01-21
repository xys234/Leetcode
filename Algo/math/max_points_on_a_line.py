"""

149. Max Points on a Line


Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6


"""

from math import gcd, inf
import fractions

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        lines = {}   # slope, intercept, count
        max_pts = 0

        if not points:
            return 0
        elif len(points) == 1:
            return 1
        else:
            max_pts = 0
            for i, p1 in enumerate(points):
                same, count = 1, {}
                for j, p2 in enumerate(points):
                    if i == j:
                        continue
                    else:
                        if p1.x == p2.x and p1.y == p2.y and i != j:
                            same += 1
                        else:
                            x_dif, y_dif = p2.x-p1.x, p2.y-p1.y
                            div = gcd(x_dif, y_dif)
                            x_dif, y_dif = x_dif/div, y_dif/div
                            if (x_dif, y_dif) not in count:
                                count[(x_dif, y_dif)] = 1
                            else:
                                count[(x_dif, y_dif)] += 1
                current_max = same
                for c in count:
                    current_max = max(current_max, count[c]+same)
                max_pts = max(max_pts, current_max)
            return max_pts

    def maxPoints_fast(self, points):

        def gcd(m, n):
            if n == 0:
                return m
            elif m * n < 0:
                return -gcd(n, m % n)
            else:
                return gcd(n, m % n)

        def slope(p1, p2):
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            if x1 == x2:
                return x1, 0
            elif y1 == y2:
                return 0, y1
            else:
                g = gcd(x2-x1, y2-y1)
                return ((x2-x1)/g, (y2-y1)/g)

        if len(points) <= 1:
            return len(points)

        ans = 0
        for i in range(len(points)-1):
            same_pts = 1
            max_pts = 0
            count = {}
            for j in range(i+1,len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 and y1 == y2:
                    same_pts += 1
                else:
                    s = slope(points[i], points[j])
                    if s in count:
                        count[s] += 1
                    else:
                        count[s] = 1
                if count:
                    max_pts = max(max_pts, max(count.values()))
            ans = max(ans, max_pts + same_pts)
        return ans

    def maxPoints2(self, points):
        n = len(points)

        if n <= 1:
            return n
        max_count = 2
        for i in range(n):
            x1, y1 = points[i]
            count = 0
            slopes = {}
            same_pts = 0
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x2 == x1 and y2 == y1:
                    same_pts += 1
                else:
                    if x2 == x1:
                        s = float('inf')
                    else:
                        s = fractions.Fraction(y2-y1, x2-x1)
                    if s in slopes:
                        slopes[s] += 1
                    else:
                        slopes[s] = 1
                    count = max(count, slopes[s])
            max_count = max(max_count, count+same_pts+1)

        return max_count


if __name__ == '__main__':

    sol = Solution()
    method = sol.maxPoints2

    cases = [
        # (method, ([[1,1],[2,2],[3,3]],), 3),
        # (method, ([[1,1],[1,1],[1,1]],), 3),
        # (method, ([[1,1],[1,1],[2,3]],), 3),
        # (method, ([[0,0],[0,0]],), 2),
        # (method, ([[0,0],[0,0],[0,0],[0,0]],), 4),
        # (method, ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],), 4),
        # (method, ([[3,1],[12,3],[3,1],[-6,-1]],), 4),
        (method, ([[94911150, 94911151],[94911151, 94911152],[0,0]],), 2),
        # (method, ([[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]],), 6),
        # (method, ([[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],
        #            [-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],
        #            [60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]],), 12),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))