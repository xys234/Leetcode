"""

665. Non-decreasing Array

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].


"""

class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':

        if len(nums) <= 1:
            return True

        count, first = 0, -1
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if first < 0:
                    first = i
                count += 1
            if count > 1:
                return False

        if 0 < first < len(nums)-2:
            if nums[first] > nums[first+2] and nums[first+1] < nums[first-1]:
                return False
        # elif first >= len(nums)-2:
        #     if nums[first+1] < nums[first-1]:
        #         return False
        return True


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.checkPossibility, ([4,2,3],), True),
        (sol.checkPossibility, ([4,2,1],), False),
        (sol.checkPossibility, ([1,3,2],), True),
        (sol.checkPossibility, ([1,2,4,5,3],), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))