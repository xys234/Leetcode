"""
547. Friend Circles (Medium)

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C,
then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

Time: O(n)
Space: O(n)

"""

from typing import List
from collections import Counter


class Solution:
    def findCircleNum1(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        num_circles = 0
        visited = set()
        frontier = []
        next = self.hasunvisited(M, visited)
        while next is not None:
            num_circles += 1
            frontier.clear()
            frontier.append(next)
            while frontier:
                cur = frontier.pop(0)
                visited.add(cur)
                nodes = self.getnodes(cur, visited, M)
                frontier.extend(nodes)
            next = self.hasunvisited(M, visited)
        return num_circles

    def getnodes(self, node, visited, mat):
        res = []
        for j in range(len(mat[node])):
            if j not in visited and mat[node][j] == 1:
                res.append(j)
        return res

    def hasunvisited(self, mat, visited):
        for i in range(len(mat)):
            if i not in visited:
                return i
        return None

    def findCircleNum(self, M: List[List[int]]) -> int:
        r = len(M)
        visited, count = set(), 0

        def dfs(row):
            for j in range(r):
                if M[row][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(r):
            if i not in visited:
                count += 1
                dfs(i)              # all friends for i
        return count


if __name__ == "__main__":
    sol = Solution()

    cases = [

        (sol.findCircleNum, ([[1,1,0],[1,1,0],[0,0,1]],), 2),
        (sol.findCircleNum, ([[1, 1, 0], [1, 1, 1], [0, 1, 1]],), 1),
        (sol.findCircleNum, ([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],), 1),
        (sol.findCircleNum, ([[1,0,0],[0,1,0],[0,0,1]],), 3),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i + 1, str(expected), str(ans)))