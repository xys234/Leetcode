"""

15. 3Sum (Medium)

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Space complexity: O(1)
Time complexity:  O(n^2)

"""


class Solution(object):
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        two_sum = {}
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in two_sum:
                    two_sum[nums[i] + nums[j]] = set()
                (two_sum[nums[i] + nums[j]]).add(tuple([i,j]))
        for k in range(len(nums)):
            if -nums[k] in two_sum:
                for s in two_sum[-nums[k]]:
                    if k not in s:
                        res.append(sorted([nums[k], nums[s[0]], nums[s[1]]]))
        return list(set([(r[0],r[1],r[2]) for r in res]))

    def threeSum3(self, nums):
        if len(nums) == 0:
            return []
        nums, i, res = sorted(nums), 0, []
        while i < len(nums) - 2 and nums[i] <= 0:
            if nums[i] != nums[i-1] or i == 0:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while k > j and nums[k] == nums[k + 1]:
                            k -= 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1

            i += 1
        return res

    def threeSum(self, nums):
        res = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:         # number of addition operations matter.
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res

    def threeSum4(self, nums):

        n = len(nums)
        nums.sort()
        res = []
        k = n - 1
        while k >= 0:
            for t in self.twosum(nums, k, -nums[k]):
                res.append(t+[nums[k]])
            while k >= 0 and nums[k] == nums[k-1]:
                k -= 1
            k -= 1

        return res

    def twosum(self, nums, end_pos, target):
        """
        Find all pairs that add up to target for sub-array nums[:end_pos]
        :param end_pos:
        :param target:
        :return:
        """

        res = []
        l, r = 0, end_pos - 1
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[l], nums[r]])
                l_val = nums[l]
                while l < r and l_val == nums[l]:
                    l += 1
                r_val = nums[r]
                while l < r and r_val == nums[r]:
                    r -= 1

            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return res

    def threeSum5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        instances = {}
        for n in nums:
            if n in instances:
                instances[n] += 1
            else:
                instances[n] = 1
        values = []
        result = []
        for n, count in sorted(instances.iteritems()):
            values.append(n)
            if n == 0 and count >= 3:
                result.append([0, 0, 0])
            elif n != 0 and count >= 2:
                third = -2 * n
                if third in instances:
                    if n < third:
                        result.append([n, n, third])
                    else:
                        result.append([third, n, n])
        # any sums involving duplicate values were handled above
        nvalues = len(values)
        while nvalues >= 3:
            floor = -(values[nvalues - 1] + values[nvalues - 2])
            ceiling = -(values[0] + values[1])
            if floor > ceiling:
                return []
            iLeft = nvalues
            iRight = -1
            for i in range(nvalues):
                if values[i] >= floor:
                    iLeft = i
                    break
            for i in range(nvalues - 1, -1, -1):
                if values[i] <= ceiling:
                    iRight = i
                    break
            if iLeft == 0 and iRight == nvalues - 1:
                break
            values = values[iLeft:iRight + 1]
            nvalues = len(values)
        if nvalues < 3:
            return result

        for i in range(nvalues - 2):
            v1 = values[i]
            if v1 >= 0:
                break
            for j in range(i + 1, nvalues - 1):
                v2 = values[j]
                v3 = -(v1 + v2)
                if v3 <= v2:
                    break
                if v3 in instances:
                    result.append([v1, v2, v3])
        return result


if __name__ == "__main__":

    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-4, -2, -1]
    # nums = [0, 0, 0, 0]
    sol = Solution()
    method = sol.threeSum4

    cases = [
        (method, ([-1, 0, 1, 2, -1, -4],), [[-1, 0, 1], [-1, -1, 2]]),
        (method, ([0,0,0,0],), [[0,0,0]]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))