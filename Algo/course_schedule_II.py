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
        if not cycle_detected:
            visited[i] = True
            cycle_stack[i] = True
            cycle_detected = False
            for j in adj[i]:
                if not visited[j]:
                    if self.topo_util_cycle(j, adj, stack, cycle_stack, cycle_detected, visited):
                        cycle_detected = True
                elif cycle_stack[j]:
                    cycle_detected = True
            cycle_stack[i] = False
            if not cycle_detected:
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
        cycle_detected = False
        for i in range(len(adj)):
            if not visited[i]:
                self.topo_util_cycle(i, adj, stack, cycle_stack, cycle_detected, visited)
        return stack

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj = self.to_adj(numCourses, prerequisites)
        stack = self.topo_sort(adj)
        return stack[::-1]


if __name__=='__main__':
    # numCourses, prerequisites = 6, [[0,1],[0,2],[1,3],[3,4],[3,5]]
    # numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
    numCourses, prerequisites = 6, [[0,1],[0,2],[1,3],[3,4],[5,3],[4,5]]

    sol = Solution()
    # print(sol.findOrder(numCourses, prerequisites))

    adj = sol.to_adj(numCourses, prerequisites)
    print(sol.topo_sort_cycle(adj))