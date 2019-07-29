"""

406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater than
or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: p[0])
        n = len(people)
        ans = [[] for _ in range(n)]

        for i, p in enumerate(people):
            if i == 0:
                ans[p[1]] = p
            elif p[1] == 0 and not ans[0]:
                ans[0] = p
            else:
                count, insertion_point = 0, p[1]

                # find the next empty space at/after insertion point
                while len(ans[insertion_point]) != 0:
                    insertion_point += 1

                # how many people taller
                for j in range(insertion_point):
                    if len(ans[j]) == 0 or ans[j][0] >= p[0]:
                        count += 1

                if count >= p[1]:
                    ans[insertion_point] = p
                else:
                    for j in range(insertion_point+1, n):
                        if len(ans[j]) == 0 or ans[j][0] >= p[0]:
                            count += 1
                            if count >= p[1]:
                                ans[j] = p
                                break
        return ans

    def reconstructQueue_solution(self, people: List[List[int]]) -> List[List[int]]:

        people = sorted(people, key=lambda p: (-p[0], p[1]))

        res = []
        for p in people:
            res.insert(p[1], p)

        return res


if __name__ == '__main__':
    sol = Solution()
    method = sol.reconstructQueue_solution

    cases = [
        (method, ([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],), [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))