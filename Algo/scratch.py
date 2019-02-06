
from math import gcd

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 1:
            return len(points)

        max_pts = 0
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                pts = 2
                for k in range(len(points)):
                    if k != i and k != j:
                        x3, y3 = points[k][0], points[k][1]
                        if x1 == x2 and y1 == y2:
                            if x1 == x3 and y1 == y3:
                                pts += 1
                        elif x1 == x2 == x3 and y1 != y2:
                            pts += 1
                        elif y1 == y2 == y3 and x1 != x2:
                            pts += 1
                        else:
                            left = (y2 - y1)*x3
                            right = (x2 - x1)*y3 + (y2 - y1)*x1 - y1*(x2-x1)
                            if left == right:
                                pts += 1
                max_pts = max(max_pts, pts)
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

if __name__=='__main__':
    sol = Solution()

    cases = [
        # (sol.maxPoints_fast, ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],), 4),
        (sol.maxPoints_fast, ([[2,3],[3,3],[-5,3]],), 3),
        # (sol.maxPoints_fast, ([[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]],), 6),
        # (sol.maxPoints_fast, ([[0,0],[0,0]],), 2),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))

