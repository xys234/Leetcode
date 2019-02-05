"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n > 1:
            p1 = 0   # first zero
            while p1 < n and nums[p1] != 0:
                p1 += 1

            p2 = p1 + 1
            while p2 < n and nums[p2] == 0:
                p2 += 1

            while p2 < n:   # there are no non-zeros till the end
                nums[p1], nums[p2] = nums[p2], nums[p1]
                while p1 < n and nums[p1] != 0:
                    p1 += 1
                if p1 == n:
                    break
                while p2 < n and nums[p2] == 0:
                    p2 += 1
            return nums

if __name__=='__main__':

    sol = Solution()

    cases = [

        # (sol.moveZeroes, ([0,1,0,3,1,12,0],), [1,3,1,12,0,0,0]),
        (sol.moveZeroes, ([0,0],), [0,0]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))