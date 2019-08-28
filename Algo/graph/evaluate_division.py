"""

399.
Medium

"""

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}
        for eq, val in zip(equations, values):
            if eq[0] not in g:
                g[eq[0]] = [(eq[1], val)]
            else:
                g[eq[0]].append((eq[1], val))

            if eq[1] not in g:
                g[eq[1]] = [(eq[0], 1.0 / val)]
            else:
                g[eq[1]].append((eq[0], 1.0 / val))

        visited = {k:False for k in g.keys()}

        def dfs(n, d):
            visited[n] = True
            if n not in g or d not in g:
                return -1

            if n == d:
                return 1

            for nei in g[n]:
                if not visited[nei[0]]:
                    v = dfs(nei[0], d)
                    if v > 0:
                        return nei[1]*v
            return -1

        ans = []
        for query in queries:
            visited = {k:False for k in g.keys()}
            ans.append(dfs(query[0], query[1]))
        return ans


if __name__ == '__main__':
    sol = Solution()
    method = sol.calcEquation

    cases = [
        # (method, ([["a", "b"], ["b", "c"]],[2.0, 3.0],[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]), [6.0, 0.5, -1.0, 1.0, -1.0 ]),
        (method, ([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]), [360.0,0.00833,20.0,1.0,-1.0,-1.0]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
