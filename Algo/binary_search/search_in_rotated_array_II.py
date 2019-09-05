"""

81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        res = False
        if not nums:
            return False

        pivot = self.find_pivot(nums, 0, len(nums)-1)
        if pivot == -1 or pivot == len(nums)-1:
            res = self.binary_search(nums, target, 0, len(nums) - 1)
        elif nums[pivot] == target:
            res = pivot
        else:
            if nums[0] <= target:
                res = self.binary_search(nums, target, 0, pivot)
            else:
                res = self.binary_search(nums, target, pivot+1, len(nums)-1)
        return res >= 0

    def binary_search(self, nums, target, low, high):
        """
        Standard binary search in an array with distinct elements
        :param nums:
        :param target:
        :param low:
        :param high:
        :return:
        """

        while low <= high:
            mid = int((low + high) / 2)  # floor
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def find_pivot(self, nums, low, high):
        """
        find the index of the pivot element in the array;
        :param nums:
        :param low:
        :param high:
        :return:

        for [3, 4, 5, 6, 1, 2]. return 3 (the index of 6)
        if it is fully sorted,  return the last element

        """

        if low > high:
            return -1

        if low == high:
            return low

        mid = int((low+high)/2)
        if mid < high and nums[mid] > nums[mid+1]:
            return mid
        elif mid > low and nums[mid] < nums[mid-1]:
            return mid-1
        elif nums[mid] < nums[low]:
            return self.find_pivot(nums, low, mid-1)
        elif nums[mid] == nums[low]:
                return self.find_pivot(nums, low+1, high)
        else:
            return self.find_pivot(nums, mid+1, high)


if __name__=='__main__':

    sol = Solution()

    cases = [
        # (sol.find_pivot, ([3,4,5,6,7,1,2], 0, 6), 4),
        # (sol.find_pivot, ([1,2,3,4], 0, 3), 3),
        # (sol.find_pivot, ([1,1,3], 0, 2), 2),
        # (sol.find_pivot, ([3,3,1], 0, 2), 1),
        # (sol.find_pivot, ([3,3,3], 0, 2), 2),
        # (sol.find_pivot, ([3,3,1,2,3], 0, 4), 1),
        # (sol.binary_search, ([1,2,3,4], 2, 0, 3), 1),
        # (sol.binary_search, ([1,2,3,4], 5, 0, 3), -1),
        # (sol.binary_search, ([1,2,3,4], 0, 0, 3), -1),
        # (sol.binary_search, ([1], 0, 0, 0), -1),
        # (sol.binary_search, ([1], 1, 0, 0), 0),
        # (sol.binary_search, ([1, 1, 3], 3, 0, 2), 2),
        # (sol.search, ([4,5,6,7,0,1,2], 0), True),
        # (sol.search, ([4,5,6,7,0,1,2], 3), False),
        # (sol.search, ([], 3), False),
        # (sol.search, ([1], 1), True),
        # (sol.search, ([1,1,3], 3), True),
        # (sol.search, ([3,1], 3), True),
        # (sol.search, ([2,5,6,0,0,1,2], 0), True),
        # (sol.search, ([2,5,6,0,0,1,2], 3), False),
        # (sol.search, ([1,1,2,1,1,1,1,1,1], 2), True),
        (sol.search, ([1]*4+[2]+[1]*8, 2), True),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
