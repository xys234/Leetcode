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


"""


class Solution:
    def monotoneIncreasingDigits(self, N: 'int') -> 'int':
        num = str(N)
        for i in range(len(num)-1,-1,0):
            if i >= 1 and num[i-1] >= num[i]:
                num[i-1] = str(int(num[i-1])-1)
                num[i] = '9'
