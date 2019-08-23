"""

996.
Hard

"""

import collections
from typing import List


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        count = collections.Counter(A)
        graph = {x:[] for x in count}

        def is_square(num):
            return int(num**0.5)**2 - num == 0

        for i in count:
            for j in count:
                if is_square(i+j):
                    graph[i].append(j)

        # find the number of hamiltonian paths starting from n.
        def dfs(n, todo):
            # mark the node as visited
            count[n] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for nei in graph[n]:
                    if count[nei]:
                        ans += dfs(nei, todo-1)

            count[n] += 1
            return ans

        return sum(dfs(x, len(A)-1) for x in count)


