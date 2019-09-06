"""
557. Reverse Words in a String III (Easy)

Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.


"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        j = 0
        res = list()
        while i < len(s) and j < len(s):
            if s[j] == " ":
                res.append(s[i:j][::-1])
                j += 1
                i = j
            elif j == len(s) - 1:
                res.append(s[i:j+1][::-1])
                j += 1
            else:
                j += 1
        return " ".join(res)


if __name__ == "__main__":

    sol = Solution()
    s = "Let's take LeetCode contest"
    print(sol.reverseWords(s))