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
        cycle = {}

        def dfs(node, path, cycle):
            status[node] = visiting
            for neighbor in graph[node]:
                if neighbor not in cycle and status[neighbor] == unvisited:
                    dfs(neighbor, path + [neighbor], cycle)
                elif status[neighbor] == visiting:
                    c = self.scan_path(path, neighbor)
                    cycle.update(c)
                    return
            status[node] = visited

        for j in range(n):
            if status[j] == unvisited and j not in cycle:
                dfs(j, [j], cycle)

        ans = []
        for j in range(n):
            safe = True
            for neighbor in graph[j]:
                if neighbor in cycle:
                    safe = False
                    break
            if safe:
                ans.append(j)
        return ans

    def scan_path(self, path, node):
        c, ind = {}, -1
        for i, n in enumerate(path):
            if n == node:
                ind = i
                break

        for i in range(ind, len(path)):
            c[path[i]] = i
        return c


if __name__ == '__main__':
    sol = Solution()

    cases = [
        # (sol.eventualSafeNodes, ([[1,2],[2,3],[5],[0],[5],[],[]],), [2,4,5,6]),
        # (sol.eventualSafeNodes, ([[1,2,3,4],[1,2,3,4],[3,4],[4],[]],), [2,3,4]),
        (sol.eventualSafeNodes, ([[1,3,4],[0,8],[2,5,6,9],[8],[7,9],[1,6,7],[7,8],[],[9],[9]],), [7]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))