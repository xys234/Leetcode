'''
(Medium)

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.




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

if __name__ == "__main__":
    
    Sol = Solution() 
    
    s = "bcdb"
    assert Sol.lengthOfLongestSubstring(s) == 3

    s = "bcd"
    assert Sol.lengthOfLongestSubstring(s) == 3

    s = "dvdf"
    assert Sol.lengthOfLongestSubstring(s) == 3
 
    s = "b"
    assert Sol.lengthOfLongestSubstring(s) == 1
 
    s = "bbbb"
    assert Sol.lengthOfLongestSubstring(s) == 1

    s = "pwwwkew"
    assert Sol.lengthOfLongestSubstring(s) == 3

    s = "abcabcbb"
    assert Sol.lengthOfLongestSubstring(s) == 3  

    s = "anviaj"
    assert Sol.lengthOfLongestSubstring(s) == 5  

    long_s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"*1000
    assert Sol.lengthOfLongestSubstring(s) == len(long_s)