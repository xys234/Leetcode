class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, v in enumerate(nums):
            if v in nums_dict:
                nums_dict[v].append(i)
            else:
                nums_dict[v] = [i]

        for i, v in enumerate(nums):
            indices = nums_dict.get(target - v, [])
            if indices:
                for j in indices:
                    if j != i:
                        return i, j
        return -1, -1

if __name__ == "__main__":
    sol = Solution()

    # nums = [2, 7, 11, 15]
    # target = 9
    # print(sol.twoSum(nums, target))
    #
    # nums = [3, 2, 4]
    # target = 6
    # print(sol.twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print(sol.twoSum(nums, target))