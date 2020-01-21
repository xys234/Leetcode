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

    def checkPossibility2(self, nums):
        n = len(nums)
        pos, pairs = 0, 0
        for i, num in enumerate(nums):
            if i < n - 1 and num > nums[i+1]:
                pairs += 1
                if pairs == 1:
                    pos = i
                if pairs >= 2:
                    return False

        if 0 < pos < n - 2 and nums[pos + 1] < nums[pos - 1] and nums[pos] > nums[pos+2]:
            return False
        return True


if __name__=='__main__':

    sol = Solution()
    method = sol.checkPossibility2

    cases = [
        (method, ([4,2,3],), True),
        (method, ([4,2,1],), False),
        (method, ([1,3,2],), True),
        (method, ([1,2,4,5,3],), True),
        (method, ([3,4,2,3],), False),
        (method, ([-1,4,2,3],), True),
        (method, ([2,3,3,2,4],), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))