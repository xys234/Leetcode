"""

171. Excel Sheet Column Number (Easy)

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        colnum = 0
        for c in range(len(s)):
            colnum += (ord(s[c]) - ord("A") + 1)*pow(26,len(s)-c-1)
        return colnum

if __name__ == "__main__":
    sol = Solution()

    s = "A"
    print(sol.titleToNumber(s))

    s = "Z"
    print(sol.titleToNumber(s))

    s = "AB"
    print(sol.titleToNumber(s))

    s = "BA"
    print(sol.titleToNumber(s))