"""

47.

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


"""

class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        nums.sort()
        used = [False for _ in nums]
        res = []

        def recurse(solution):
            if len(solution) == n:
                res.append(solution[:])
                return

            prev = -1           # last element examined
            for i, num in enumerate(nums):
                if used[i] or (prev >= 0 and nums[prev] == num):
                    continue
                used[i] = True
                recurse(solution + [num])
                used[i] = False
                prev = i

        recurse([])
        return res


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.permuteUnique, ([1, 1, 2], ), [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))