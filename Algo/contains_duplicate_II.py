"""
219. Easy

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

2019.02.07 Reviewed

"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        nums_dict = {}

        # convert to a dict
        for i, n in enumerate(nums):
            if n not in nums_dict:
                nums_dict[n] = [i]
            else:
                nums_dict[n].append(i)
                if i-nums_dict[n][-2] <= k:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        num_index = {}
        for i, _ in enumerate(nums):
            if nums[i] not in num_index:
                num_index[nums[i]] = i
            else:
                if i - num_index[nums[i]] <= k:
                    return True
                else:
                    num_index[nums[i]] = i
        return False

    def containsNearbyDuplicate3(self, nums, k):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, min(i+k+1, n)):
                if nums[i] == nums[j]:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    method = sol.containsNearbyDuplicate3

    cases = [
        (method, ([1, 2, 3, 1], 3), True),
        (method, ([1,0,1,1], 1), True),
        (method, ([1,2,3,1,2,3], 2), False),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
