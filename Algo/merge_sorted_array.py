"""

88. Merge Sorted Array (Easy)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.


"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        res = list(range(m+n))
        if m == 0:
            nums1[:] = nums2[:]

        elif n > 0:
            i = j = k = 0
            while i < m and j < n:
                if nums1[i] <= nums2[j]:
                    res[k] = nums1[i]
                    i += 1
                else:
                    res[k] = nums2[j]
                    j += 1
                k += 1
            if m - i < n - j:
                res[k::] = nums2[j:n]
            else:
                res[k::] = nums1[i:m]
            nums1[:] = res[:]

if __name__ == "__main__":
    sol = Solution()

    # nums1 = [3,5,7,9,100,100,100]
    # nums2 = [2,4,11]
    #
    # sol.merge(nums1,4,nums2,3)
    # print(nums1)

    # nums1 = [1]
    # nums2 = [0]
    # sol.merge(nums1, 1, nums2, 0)

    # nums1 = [1,0]
    # nums2 = [2]

    nums1 = [4, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]

    sol.merge(nums1, 1, nums2, 5)

    print(nums1)