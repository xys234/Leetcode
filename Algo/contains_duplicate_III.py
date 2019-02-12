"""

220. medium

Given an array of integers, find out whether there are two distinct indices i and j in the array such that
the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j
is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

2019.02.07 Reviewed; Group numbers into ranges with centers at t, 2t, 3t...,
"""


class Solution:
    def containsNearbyAlmostDuplicate_brute_force(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        for i, _ in enumerate(nums):
            for d in range(-k, k+1):
                if d != 0 and i+d >= 0 and i+d < len(nums):
                    if abs(nums[i] - nums[i+d]) <=t:
                        return True
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        key_to_val = {}
        for num in nums:
            key = (num) // (t+1)
            if key in key_to_val:
                return True
            elif key + 1 in key_to_val and num - key_to_val[key+1] <= t:
                return True
            elif key - 1 in key_to_val and num - key_to_val[key-1] <= t:
                return True
            key_to_val[key] = num
        return False

if __name__ == '__main__':
    cases = [
        # ([1, 2, 3, 1], 3, 0),
        # ([1,0,1,1], 1, 2),
        ([1,5,9,1,5,9], 2, 3),
        # ([3,6,0,4], 2, 2),

    ]
    s = Solution()
    for case in cases:
        nums, k, t = case
        print(s.containsNearbyAlmostDuplicate(nums, k, t))