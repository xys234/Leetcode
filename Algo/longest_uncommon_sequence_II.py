"""

522. Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and
this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters
without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and
an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence.
If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].



"""


class Solution:

    def is_sub_sequence(self, sub, str):
        """
        Determine if sub is a sub-sequence of str
        :param sub: a string
        :param str: a string
        :return:
        """
        i = 0
        for s in str:
            if s == sub[i]:
                i += 1
            if i == len(sub):
                return True
        return False

    # Brute force algorithm
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        strs.sort(key=len, reverse=True)
        checked = {}
        for i, s in enumerate(strs):
            found = False
            if not checked and len(strs[i]) > len(strs[i+1]):
                return len(strs[i])
            elif s in checked:
                continue
            else:
                for j, k in enumerate(strs):            # need to check all the other elements
                    if j != i and self.is_sub_sequence(s, k):
                        found = True
                        break
                checked[s] = len(s)
                if not found:
                    return len(s)
        return -1




if __name__=='__main__':
    sol = Solution()
    cases = {
        ("aba", "cdc", "eae"): 3,
        ("aaa", "aaa", "aa"): -1,
        ("aabbcc", "aabbcc","bc","bcc","aabbccc"): 7,
        ("aabbcc", "aabbcc","cb"): 2,
        ("a","b","c","d","e","f","a","b","c","d","e","f"): -1

    }

    for input, output in cases.items():
        assert sol.findLUSlength(list(input)) == output, (sol.findLUSlength(list(input)), output)
