"""

532

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers
in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].


"""



class Solution:
    def findPairs(self, nums: 'List[int]', k: 'int') -> 'int':

        if k < 0:
            return 0

        n1 = dict()
        for i, n in enumerate(nums):
            if n in n1:
                n1[n].append(i)
            else:
                n1[n] = [i]
        visited = set()
        for i in range(len(nums)):
            if nums[i] + k in n1:
                for j in n1[nums[i]+k]:
                    if j != i and (nums[i], nums[j]) not in visited and (nums[j], nums[i]) not in visited:
                        visited.add((nums[i], nums[j]))
            if nums[i] - k in n1:
                for j in n1[nums[i]-k]:
                    if j != i and (nums[i], nums[j]) not in visited and (nums[j], nums[i]) not in visited:
                        visited.add((nums[i], nums[j]))
        return len(visited)

    def findPairs_fast(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0

        pairs = set()
        m = {}
        for i, num in enumerate(nums):
            if i == 0:
                m[num] = i
                continue

            target = num - k
            if target in m:
                pairs.add((num, target) if num <= target else (target, num))

            target = num + k
            if target in m:
                pairs.add((num, target) if num <= target else (target, num))

            m[num] = i

        return len(pairs)


if __name__=='__main__':

    sol = Solution()

    cases = [
        (sol.findPairs, ([1,3,1,5,4],0), 1),
        (sol.findPairs, ([3, 1, 4, 1, 5],2), 2),
        (sol.findPairs, ([1, 2, 3, 4, 5],1), 4),
        (sol.findPairs, ([1, 2, 3, 4, 5],-1), 0),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))