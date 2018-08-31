"""
X is a good number if after rotating each digit individually by 180 degrees,
we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
2 and 5 rotate to each other; 6 and 9 rotate to each other,
and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].


"""


class Solution:
    def rotate_number(self, n):
        """

        :param n: is an integer
        :return: the number after rotation
        """
        rotations = {
            0: 0,
            1: 1,
            2: 5,
            3: None,
            4: None,
            5: 2,
            6: 9,
            7: None,
            8: 8,
            9: 6
        }
        str_n = []
        for s in str(n):
            if rotations[int(s)] is None:
                return None
            else:
                str_n.append(str(rotations[int(s)]))

        return int("".join(str_n))


    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        result = 0
        for n in range(1, N+1):
            rotate = self.rotate_number(n)
            if rotate and n != rotate:
                result += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    cases = [
        (10, 4),
        (2, 1),
        (857, 247)


    ]

    # print(sol.rotate_number(857))

    for c in cases:
        assert sol.rotatedDigits(c[0]) == c[1], (sol.rotatedDigits(c[0]), c[1])
