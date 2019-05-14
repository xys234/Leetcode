"""

46.

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


"""


class Solution:
    def permute(self, nums):
        n = len(nums)
        used = [False for _ in nums]
        res = []

        def recurse(solution):
            if len(solution) == n:
                res.append(solution[:])

            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    recurse(solution + [num])
                    used[i] = False

        recurse([])
        return res


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.permute, ([1, 2, 3], ), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))