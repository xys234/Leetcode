"""
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.


"""



class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        # Save the types of jewels
        num_jewels = 0
        for s in S:
            if s in J:
                num_jewels += 1

        return num_jewels


if __name__=='__main__':
    sol = Solution()
    cases = {
        ("aA", "aAAbbbb"):3,
        ("z", "ZZ"):0

    }

    for input, output in cases.items():
        assert sol.numJewelsInStones(input[0], input[1]) == output, (sol.numJewelsInStones(input[0], input[1]), output)


