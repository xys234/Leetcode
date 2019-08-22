"""

996. Number of Squareful Arrays
Hard


"""

from typing import List
from math import sqrt

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        perms = self.permutation(A)
        ans = 0
        for perm in perms:
            sums = []
            for i, num in enumerate(perm):
                if i == 0:
                    sums.append(num+perm[i+1])
                elif i == len(perm)-1:
                    sums.append(num+perm[i-1])
                else:
                    sums.append(num + perm[i + 1])
                    sums.append(num + perm[i - 1])

            found = False
            for s in sums:
                if not self.is_square(s):
                    found = True
                    break
            if not found:
                ans += 1

        return ans

    def is_square(self, n):
        return int(sqrt(n))**2 == n

    def permutation(self, nums):
        """
        Generate distinct permutations
        :param nums:
        :return:

        [2, 2, 4] has only 3 distinct permutations not 6: [2, 2, 4], [2, 4, 2], [4, 2, 2]

        """

        n = len(nums)
        nums.sort()
        perm = []
        visited = [False for _ in range(n)]

        def dfs(cur_perm):
            if len(cur_perm) == n:
                perm.append(cur_perm[:])
                return

            prev = -1
            for i, num in enumerate(nums):
                if not visited[i] and (prev < 0 or num != nums[prev]):
                    visited[i] = True
                    dfs(cur_perm + [nums[i]])
                    visited[i] = False
                    prev = i

        dfs([])
        return perm


if __name__ == "__main__":

    sol = Solution()
    method = sol.numSquarefulPerms

    cases = [
        # (method, ([1, 17, 8], ), 2),
        (method, ([1,1,1,4,5,1,4,2,2,1,2,2], ), 2),
        # (method, ([2, 2, 4], ), 2),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i + 1, str(expected), str(ans)))
