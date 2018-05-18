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


if __name__ == "__main__":

    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-4, -2, -1]
    # nums = [0, 0, 0, 0]
    print(sol.threeSum(nums))