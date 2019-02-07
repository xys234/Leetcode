'''


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
You may assume that there are no duplicate edges in the input prerequisites.



'''


class Solution:
    def edges_to_adj(self, edges):
        '''

        :param edges: a list of edges. Each edge is a two-element list
        :return: adjacency lists. a dictionary of lists. {v: l(v)}. l(v) is a list of nodes reachable from v
        '''

        adj = {}
        for e in edges:
            if e[0] in adj:
                adj[e[0]].append(e[1])
            else:
                adj[e[0]] = [e[1]]
        return adj


    def is_cycle_util(self, v, adj, visited, recur_stack):
        visited[v] = True
        recur_stack[v] = True

        if v in adj:
            for n in adj[v]:
                if not visited[n]:
                    if self.is_cycle_util(n, adj, visited, recur_stack):
                        return True
                    else:
                        visited[n] = True
                elif recur_stack[n]:
                    return True

        # Pop v from the recursive stack
        recur_stack[v] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int. Number of courses.
        :type prerequisites: List[List[int]]
        :rtype: bool

        use bfs to determine if there is a cycle

        """
        adj = self.edges_to_adj(prerequisites)
        visited = [False for i in range(numCourses)]
        recur_stack = [False for i in range(numCourses)]
        for i in range(numCourses):
            if i in adj:
                if self.is_cycle_util(i, adj, visited, recur_stack):
                    return False
            else:
                visited[i] = True
        return True

    def canFinish2(self, numCourses, prerequisites):
        if numCourses <= 1 or len(prerequisites) == 0:
            return True

        def buildGraph():
            g = {}
            for p in prerequisites:
                if p[1] not in g:
                    g[p[1]] = [p[0]]
                else:
                    g[p[1]].append(p[0])
            return g

        g = buildGraph()
        visited = [False for _ in range(numCourses)]

        for i in range(numCourses):
            if i not in g:
                continue
            if not visited[i]:
                q = [i]
                while q:
                    n = q.pop(0)
                    visited[n] = True
                    if n in g:
                        for neighbor in g[n]:
                            if not visited[neighbor]:
                                q.append(neighbor)
                            else:
                                return False
        return True


if __name__=='__main__':
    sol = Solution()

    cases = [
        # (sol.canFinish2, (6, [[0,1], [1,2], [2,3], [3,4], [4,5], [5,1]],), False),
        # (sol.canFinish2, (2, [[1,0]],), True),
        # (sol.canFinish2, (2, [[0,1],[1,0]],), False),
        # (sol.canFinish2, (3, [[1,0],[2,0]],), True),
        # (sol.canFinish2, (2, [[0,1]],), True),
        (sol.canFinish2, (3, [[2,0],[2,1]],), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))


