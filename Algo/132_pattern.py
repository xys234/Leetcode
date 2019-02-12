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
        Space complexity: O(n)

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



if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.find132pattern, ([1,2,3,4],), False),
        (sol.find132pattern, ([3,1,4,2],), True),
        (sol.find132pattern, ([3,5,0,3,4],), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))