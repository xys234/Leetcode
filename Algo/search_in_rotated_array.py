"""

30.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Time complexity: O(log n)
Space complexity: O(1)

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        pivot = self.find_pivot(nums, 0, len(nums)-1)
        if pivot == -1 or pivot == len(nums)-1:
            return self.binary_search(nums, target, 0, len(nums) - 1)
        elif nums[pivot] == target:
            return pivot
        else:
            if nums[0] <= target:
                return self.binary_search(nums, target, 0, pivot)
            else:
                return self.binary_search(nums, target, pivot+1, len(nums)-1)

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
        if mid > low and nums[mid] < nums[mid-1]:
            return mid-1
        if nums[low] > nums[mid]:
            return self.find_pivot(nums, low, mid-1)
        return self.find_pivot(nums, mid+1, high)

    def findPivot(self, arr, low, high):

        # base cases
        if high < low:
            return -1
        if high == low:
            return low

        mid = int((low + high) / 2)

        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return (mid - 1)
        if arr[low] >= arr[mid]:
            return self.findPivot(arr, low, mid - 1)
        return self.findPivot(arr, mid + 1, high)

if __name__=='__main__':

    sol = Solution()

    cases = [
        # (sol.find_pivot, ([3,4,5,6,7,1,2], 0, 6), 4),
        # (sol.find_pivot, ([1,2,3,4], 0, 3), -1),
        # (sol.find_pivot, ([1,3,5], 0, 2), 2),
        # (sol.findPivot, ([1,3,5], 0, 2), 2),
        # (sol.binary_search, ([1,2,3,4], 2, 0, 3), 1),
        # (sol.binary_search, ([1,2,3,4], 5, 0, 3), -1),
        # (sol.binary_search, ([1,2,3,4], 0, 0, 3), -1),
        # (sol.binary_search, ([1], 0, 0, 0), -1),
        # (sol.binary_search, ([1], 1, 0, 0), 0),
        (sol.search, ([4,5,6,7,0,1,2], 0), 4),
        (sol.search, ([4,5,6,7,0,1,2], 3), -1),
        (sol.search, ([], 3), -1),
        (sol.search, ([1], 1), 0),
        (sol.search, ([3,1], 1), 1),
        (sol.search, ([3,1], 3), 0),
        (sol.search, ([1,3,5], 1), 0),
        (sol.search, ([3,5,1], 3), 0),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))

