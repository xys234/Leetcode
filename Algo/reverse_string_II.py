"""

Given a string and an integer k, you need to reverse the first k characters
for every 2k characters counting from the start of the string. If there are less than k characters left,
reverse all of them. If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]


"""


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        result = []
        # how many substrings with length 2k
        num = len(s) // (2*k)
        s1 = s[:2*k*num]
        s2 = s[2*k*num:]

        i = 0
        while len(s1) - i >= k:
            if ((i + k) / k) % 2 == 1:
                result.append(s1[i:i + k][::-1])
            else:
                result.append(s1[i:i + k])
            i += k

        if len(s2) < k:
            result.append(s2[::-1])
        elif len(s2) < 2 * k and len(s2) >= k:
            result.append(s2[:k][::-1] + s2[k:])

        return "".join(result)


if __name__ == '__main__':
    sol = Solution()
    cases = [
        ("abcdefg", 2, "bacdfeg"),
        ("abcd", 3, "cbad"),
        ("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",
         39,
         "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi")



    ]


    for c in cases:
        print(sol.reverseStr(c[0], c[1]))
        assert sol.reverseStr(c[0], c[1]) == c[2]