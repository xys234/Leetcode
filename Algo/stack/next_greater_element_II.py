"""


"""


class Solution:
    def nextGreaterElements_TLE(self, nums: 'List[int]') -> 'List[int]':
        extended_nums = nums + nums[:-1]
        next_greater = [-1 for _ in extended_nums]
        ans = []
        for i, n in enumerate(extended_nums):
            if i >= 1 and n > extended_nums[i-1]:
                curr = i - 1
                while curr >= 0 and extended_nums[i] > extended_nums[curr]:
                    if next_greater[curr] < 0:
                        next_greater[curr] = i
                    curr -= 1
        return [extended_nums[j] if j >= 0 else -1 for j in next_greater[:len(nums)]]

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(nums)
        result = [-1 for _ in range(n)]

        for nums_ptr in range(len(nums)):
            while stack and stack[-1][0] < nums[nums_ptr]:
                v, idx = stack.pop()
                result[idx] = nums[nums_ptr]

            stack.append((nums[nums_ptr], nums_ptr))

        for nums_ptr in range(len(nums)):
            while stack and stack[-1][0] < nums[nums_ptr]:
                v, idx = stack.pop()
                result[idx] = nums[nums_ptr]

        return result

if __name__=='__main__':

    sol = Solution()

    cases = [

        # (sol.nextGreaterElements, ([1,2,1],), [2,-1,2]),
        (sol.nextGreaterElements, ([4,3,1,2,1], ), [-1,4,2,4,4]),
        # (sol.nextGreaterElements, ([1,8,-1,-100,-1,222,1111111,-111111], ), [8,222,222,-1,222,1111111,-1,1]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))
