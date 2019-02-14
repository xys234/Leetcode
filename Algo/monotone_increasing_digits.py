"""

738.

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only
if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].


2019/02/14: First attempt own solution beat 100% submission

"""


class Solution:
    def monotoneIncreasingDigits(self, N: 'int') -> 'int':
        """

        :param N:
        :return:

        Time complexity: O(n)
        Space complexity: O(1)

        Greedy algorithm

        """
        num = list(str(N))
        for i in range(len(num)-1,0,-1):
            if i >= 1 and num[i-1] > num[i]:
                num[i-1] = str(int(num[i-1])-1)
                num[i] = '9'
                j = i + 1
                while j <= len(num)-1:
                    num[j] = '9'
                    j += 1

        while num and num[0] == '0':
            num.pop(0)
        return int(''.join(num))

if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.monotoneIncreasingDigits, (10,), 9),
        (sol.monotoneIncreasingDigits, (1234,), 1234),
        (sol.monotoneIncreasingDigits, (332,), 299),
        (sol.monotoneIncreasingDigits, (5879,), 5799),
        (sol.monotoneIncreasingDigits, (5876,), 5799),
        (sol.monotoneIncreasingDigits, (101,), 99),
        (sol.monotoneIncreasingDigits, (120,), 119),


             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))