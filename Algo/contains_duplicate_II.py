"""

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


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 1], 3),
        ([1,0,1,1], 1),
        ([1,2,3,1,2,3], 2),
    ]
    s = Solution()
    for case in cases:
        nums, k = case
        print(s.containsNearbyDuplicate(nums, k))