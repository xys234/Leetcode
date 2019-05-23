'''

210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
You may assume that there are no duplicate edges in the input prerequisites.

Solution:
2019.02.06 Reviewed
2019.05.23 Passed



'''


class Solution:

    def to_adj(self, numnodes, edges):
        # adj = [[]]*numnodes                   # This will create four elements sharing the same memory
        adj = [[] for i in range(numnodes)]
        for e in edges:
            adj[e[0]].append(e[1])
        return adj

    def topo_util(self, i, adj, stack, visited):
        if not visited[i]:
            visited[i] = True
            for j in adj[i]:
                self.topo_util(j, adj, stack, visited)
            stack.insert(0, i)

    def topo_util_cycle(self, i, adj, stack, cycle_stack, cycle_detected, visited):

        visited[i] = True
        cycle_stack[i] = True
        for j in adj[i]:
            if not visited[j]:
                self.topo_util_cycle(j, adj, stack, cycle_stack, cycle_detected, visited)
            elif cycle_stack[j]:
                for c in range(len(cycle_detected)):
                    cycle_detected[c] = True
        cycle_stack[i] = False
        if any(cycle_detected):
            stack.clear()
        else:
            stack.insert(0, i)
        return cycle_detected

    def topo_sort(self, adj):
        visited = [False]*len(adj)
        stack = []
        for i in range(len(adj)):
            self.topo_util(i, adj, stack, visited)
        return stack

    def topo_sort_cycle(self, adj):

        visited = [False]*len(adj)
        stack = []
        cycle_stack = [False]*len(adj)
        cycle_detected = [False]*len(adj)
        for i in range(len(adj)):
            if not visited[i] and not cycle_detected[i]:
                self.topo_util_cycle(i, adj, stack, cycle_stack, cycle_detected, visited)
        return stack

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj = self.to_adj(numCourses, prerequisites)
        stack = self.topo_sort_cycle(adj)
        return stack[::-1]

    def findOrder2(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            if p:
                graph[p[1]].append(p[0])

        unvisited, visiting, visited = 0, 1, 2
        status = [unvisited for _ in range(numCourses)]

        def dfs(node, g, sorted_graph):
            status[node] = visiting
            if g[node]:
                for v in g[node]:
                    if status[v] == visiting:
                        return False
                    if status[v] == unvisited and not dfs(v, g, sorted_graph):
                        return False
            status[node] = visited
            sorted_graph.append(node)
            return True

        sorted_g = []
        for j in range(numCourses):
            if status[j] != visited:
                if not dfs(j, graph, sorted_g):
                    return []
        return sorted_g[::-1]


if __name__ == '__main__':
    sol = Solution()

    cases = [
        (sol.findOrder2, (2, [[1, 0]],), ([0, 1],)),
        (sol.findOrder2, (4, [[1, 0], [2, 0], [3, 1], [3, 2]],), ([0, 1, 2, 3], [0, 2, 1, 3])),
        (sol.findOrder2, (1, [[]],), ([0],)),
        # (sol.findOrder2, (4, [[1,0],[2,0],[3,1],[3,2]],), True),
        # (sol.findOrder2, (4, [[2,0], [1,0], [3,1], [3,2], [1,3]],), False),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans in expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))