"""


802.
Medium

"""

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        unvisited, visiting, visited = 0, 1, 2
        n = len(graph)
        status = [unvisited for _ in range(n)]
        unsafe = {}

        def dfs(node, path, unsafe):
            status[node] = visiting
            for neighbor in graph[node]:
                if neighbor not in unsafe and status[neighbor] == unvisited:
                    dfs(neighbor, path + [neighbor], unsafe)
                elif status[neighbor] == visiting or neighbor in unsafe:
                    unsafe.update({p:1 for p in path})
                    return
            status[node] = visited

        for j in range(n):
            if status[j] == unvisited and j not in unsafe:
                dfs(j, [j], unsafe)

        ans = [i for i in range(n) if i not in unsafe]
        return ans


if __name__ == '__main__':
    sol = Solution()

    cases = [
        (sol.eventualSafeNodes, ([[1,2],[2,3],[5],[0],[5],[],[]],), [2,4,5,6]),
        (sol.eventualSafeNodes, ([[1,2,3,4],[1,2,3,4],[3,4],[4],[]],), [2,3,4]),
        (sol.eventualSafeNodes, ([[1,3,4],[0,8],[2,5,6,9],[8],[7,9],[1,6,7],[7,8],[],[9],[9]],), [7]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))