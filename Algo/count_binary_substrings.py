"""

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation:
There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.


"""


class Solution:
    def is_binary_string(self, s):
        n = len(s)
        if n % 2 != 0:
            return False
        else:
            first_half = s[0]*int(n/2) == s[:int(n/2)]
            second_half = s[int(n/2)]*int(n/2) == s[int(n/2):]
            diff = s[0] != s[int(n/2)]
            return first_half & second_half & diff


    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        for i in range(len(s)):
            for j in range(i+2,len(s)+1,2):
                if self.is_binary_string(s[i:j]):
                    print(s[i:j])
                    num += 1
        return num


if __name__=='__main__':

    sol = Solution()

    cases = [
        ["00110011", 6],
        ["10101", 4]

    ]

    for case in cases:
        # sol.countBinarySubstrings(case[0]) == case[1]
        assert sol.countBinarySubstrings(case[0]) == case[1], (sol.countBinarySubstrings(case[0]), case[1])