"""

27. Remove Elements

Easy

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.


"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        length = 0
        p1, p2 = 0, n - 1
        while p1 <= p2:
            if nums[p1] == val and nums[p2] != val:
                swap(p1, p2)
                p1 += 1
                p2 -= 1
                length += 1
            elif nums[p2] == val:
                p2 -= 1
            else:
                length += 1
                p1 += 1
        return length


if __name__ == '__main__':
    sol = Solution()
    nums, val = [0,4,4,0,4,4,4,0,2], 4
    # nums, val = [3,3], 3
    # nums, val = [2,2,3], 2
    # nums, val = [3,2,2,3], 3
    # nums, val = [0,1,2,2,3,0,4,2], 2
    length = sol.removeElement(nums, val)
    print(nums, length)
