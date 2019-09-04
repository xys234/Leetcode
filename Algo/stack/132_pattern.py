"""

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that
i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.



Similar solution: 3sum

"""


class Solution:
    def find132pattern(self, nums: 'List[int]') -> 'bool':
        """

        :param nums:
        :return:

        Time complexity: O(n^2)
        Space complexity: O(1)

        """
        n, min_element, min_index = len(nums), float("inf"), -1
        for i in range(n):
            if min_element > nums[i]:   # find the min element and the aj
                min_element, min_index = nums[i], i
            if nums[i] == min_element:  # skip elements following the min_element are equal to min_element
                continue
            for j in range(n-1, i, -1): # find ak
                if min_element < nums[j] < nums[i]:
                    return True
        return False

    def find132pattern_fast(self, nums: 'List[int]') -> 'bool':
        """

        :param nums:
        :return:

        elements in stack must be larger than third; the min element larger than third is on stop

        """
        third = -float('inf')
        stack = []
        for i in range(len(nums)-1,-1,-1):  # find the first
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:   # loop through the stack to find the best third
                third = stack.pop()
            stack.append(nums[i])

        return False

    def find132pattern3(self, nums):
        stack, third = [], -float('inf')
        for n in reversed(nums):
            if n < third:
                return True
            while stack and n > stack[-1]:    # decreasing stack.
                third = stack.pop()
            stack.append(n)
        return False


if __name__ == '__main__':

    sol = Solution()
    method = sol.find132pattern3

    cases = [

        (method, ([1,2,3,4],), False),
        (method, ([3,3,4,2],), False),
        (method, ([3,1,4,2],), True),
        (method, ([3,5,0,3,4],), True),
        (method, ([-2,1,1,-2,1,1],), False),
        (method, ([-2,1,2,-2,1,2],), True),
        (method, ([2,4,3,1],), True),
        (method, ([10,12,6,8,3,11],), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))