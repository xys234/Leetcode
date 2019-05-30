"""

690. Course Schedule III

There are n different online courses numbered from 1 to n.
Each course has some duration(course length) t and closed on dth day.
A course should be taken continuously for t days and must be finished before or on the dth day.
You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day,
and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day,
and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.


Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

Attempts:

2019-05-30:  Attempt failed.

"""

from typing import List
import heapq


class Course:
    def __init__(self, course):
        self.length = course[0]
        self.limit = course[1]

    def __lt__(self, other):
        return self.length > other.length


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses = [Course(course) for course in courses]
        # courses.sort(key=lambda c: c.limit - c.length)
        courses.sort(key=lambda c: c.limit)
        # Remove impossible courses
        courses = [course for course in courses if course.limit - course.length >= 0]

        current_total_time, sequence = 0, []
        for course in courses:

            if current_total_time + course.length <= course.limit:
                # Take the new course
                current_total_time += course.length
                heapq.heappush(sequence, course)

            else:
                latest_course = heapq.nlargest(1, sequence, key=lambda x: x.limit)[0]
                if current_total_time + course.length <= latest_course.limit:
                    heapq.heappush(sequence, course)
                    current_total_time += course.length
                else:
                    longest_course = heapq.nlargest(1, sequence, key=lambda x: x.length)[0]
                    if current_total_time - longest_course.length + course.length <= course.limit and \
                            (course.limit > longest_course.limit or course.length < longest_course.length):
                        current_total_time = current_total_time - longest_course.length + course.length
                        heapq.heappop(sequence)
                        heapq.heappush(sequence, course)
        return len(sequence)

    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        current_total_time, sequence = 0, []
        for course in courses:
            current_total_time += course[0]
            heapq.heappush(sequence, -course[0])
            if current_total_time > course[1]:
                current_total_time += sequence[0]
                heapq.heappop(sequence)
        return len(sequence)


if __name__ == '__main__':
    sol = Solution()
    method = sol.scheduleCourse2

    cases = [
        (method, ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],), 3),
        (method, ([[100, 2], [32, 50]],), 1),
        (method, ([[5, 5], [4, 6], [2, 6]],), 2),
        (method, ([[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]],), 4),
        (method, ([[9, 14], [7, 12], [1, 11], [4, 7]],), 3),
        (method, ([[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]],), 4),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
