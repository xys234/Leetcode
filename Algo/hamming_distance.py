"""

461 Hamming Distance (Easy)

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        sx = format(x, '032b')
        sy = format(y, '032b')

        hamming = 0
        for (s1, s2) in zip(sx, sy):
            if s1 != s2:
                hamming += 1
        return hamming