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

from math import gcd

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

if __name__ == '__main__':
    # coordinates = [[1,1],[2,2],[3,3]]
    # coordinates = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # coordinates = [[3,1],[12,3],[3,1],[-6,-1]]
    # coordinates = [[0,0],[94911151,94911150],[94911152,94911151]]
    coordinates = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]    # 4
    points = [Point(c[0], c[1]) for c in coordinates]
    sol = Solution()
    print(sol.maxPoints(points))