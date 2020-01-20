'''

3.
(Medium)

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.




'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        char = set()
        maxlen = 0
        maxstr = ""
        i = 0
        j = 0

        while i < len(s) and j < len(s):
            if s[j] not in char:
                char.add(s[j])
                j = j + 1
                if j - i > maxlen:
                    maxlen = j - i
                    maxstr = s[i:i+maxlen] 
                
            else:
                char.discard(s[i])   
                i = i + 1
        print(maxstr)
        return(maxlen)

    def lengthOfLongestSubstring2(self, s):
        m = {}
        start = 0
        max_len = 0

        for i, c in enumerate(s):
            if c in m:
                start = max(m[c] + 1, start)

            m[c] = i
            length = i + 1 - start
            max_len = max(max_len, length)
        return max_len


if __name__ == "__main__":
    
    sol = Solution()
    method = sol.lengthOfLongestSubstring2

    long_s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" * 1000

    cases = [
        (method, ("bcdb",), 3),
        (method, ("bcd",), 3),
        (method, ("dvdf",), 3),
        (method, ("b",), 1),
        (method, ("bbbb",), 1),
        (method, ("pwwwkew",), 3),
        (method, ("abcabcbb",), 3),
        (method, ("anviaj",), 5),
        (method, ("tmmzuxt",), 5),
        (method, (s,), len(long_s)),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
