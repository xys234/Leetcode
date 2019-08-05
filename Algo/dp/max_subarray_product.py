"""

152.
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

2019.08.03


"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:

        Time: O(n); Space: O(n)

        """

        n = len(nums)
        min_product, max_product = [0]*n, [0]*n
        min_product[0], max_product[0] = nums[0], nums[0]
        ans = 0

        for j in range(1, n):
            max_product[j] = max(nums[j], min_product[j-1]*nums[j], max_product[j-1]*nums[j])
            min_product[j] = min(nums[j], max_product[j-1]*nums[j], min_product[j-1]*nums[j])
            ans = max(ans, max_product[j])
        return ans

