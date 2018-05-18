"""

657. Judge Route Circle (Easy)

Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        # Assume a grid
        directions = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
        pos = [0, 0]

        for m in moves:
            pos[0] = pos[0] + directions[m][0]
            pos[1] = pos[1] + directions[m][1]

        if pos == [0, 0]:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()

    moves = "UD"
    print(sol.judgeCircle(moves))

    moves = "LL"
    print(sol.judgeCircle(moves))