"""
841. Keys and Rooms

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1,
and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1]
where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.

Time: O(n)
Space: O(n)

"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        number_of_rooms = len(rooms)
        if number_of_rooms == 0:
            return False

        visited = set()
        q = [0]
        visited.clear()
        visited.add(0)
        while q:
            top = q.pop(0)
            for n in rooms[top]:
                if n not in visited:
                    q.append(n)
                    visited.add(n)
                    if len(visited) == number_of_rooms:
                        return True

        if len(visited) == number_of_rooms:
            return True
        else:
            return False


if __name__ == '__main__':

        sol = Solution()

        cases = [
            (sol.canVisitAllRooms, ([[1], [2], [3], []],), True),
            (sol.canVisitAllRooms, ([[1, 3], [3, 0, 1], [2], [0]],), False),
            (sol.canVisitAllRooms, ([[]],), True),
            (sol.canVisitAllRooms, ([[1], [], [0,3], [1]],), False),
        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if ans == expected:
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))
