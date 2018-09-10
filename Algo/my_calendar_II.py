"""
Implement a MyCalendarTwo class to store your events.
A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection
(ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without
causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].


"""

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []              # use an array sorted by event start time

    def search(self, event):
        """
        find the insertion point
        :param event: (start_time, end_time)
        :return:
        """

        head = 0
        tail = len(self.calendar)
        while tail - head > 1:
            if self.calendar[(tail+head)//2][0] > event[0]:
                tail = (tail+head)//2
            elif self.calendar[(tail+head)//2][0] < event[0]:
                head = (tail+head)//2
            else:
                return (tail+head)//2
        if event[0] > self.calendar[head][0]:
            return head + 1
        else:
            return head


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if not self.calendar:
            self.calendar.append((start, end))
            return True
        else:
            nearest_index = self.search((start, end))
            left_check, right_check = 0, 0
            left_max, right_min = 0, 10**9+1
            check_lower, check_higher = max(0, nearest_index-2), min(nearest_index+2, len(self.calendar))

            if len(self.calendar) > 1:
                # get the check range, at least 2 on each side.
                for i in range(nearest_index-3, 0, -1):
                    if self.calendar[i][1] < start:
                        check_lower = min(i + 1, check_lower)
                        break
                for i in range(nearest_index+3, len(self.calendar)):
                    if self.calendar[i][0] > end:
                        check_higher = max(i - 1, check_higher)
                        break
                # check_lower, check_higher = max(0, check_lower), min(len(self.calendar)-1, check_higher)
                check_lower, check_higher = 0, len(self.calendar)-1

                for j in range(check_lower, check_higher+1):
                    if j < nearest_index:
                        if self.calendar[j][1] > start:
                            left_max = max(self.calendar[j][1], left_max)
                            left_check += 1
                    elif j == nearest_index:
                        if self.calendar[j][0] < start:
                            if self.calendar[j][1] > start:
                                left_max = max(self.calendar[j][1], left_max)
                                left_check += 1
                        elif self.calendar[j][0] < end:
                            right_min = min(right_min, self.calendar[j][0])
                            right_check += 1
                    else:
                        if self.calendar[j][0] < end:
                            right_min = min(right_min, self.calendar[j][0])
                            right_check += 1

        if left_check >= 2 or right_check >= 2 or right_min < left_max:
            return False
        else:
            left = self.calendar[:nearest_index]
            right = self.calendar[nearest_index:]
            self.calendar = left + [(start, end)] + right
            return True


if __name__ == '__main__':

    obj = MyCalendarTwo()
    # case = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    # case = [[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
    # case = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
    # case = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
    # case = [[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25], [8,17], [24,33], [23,28], [21, 27]]
    # case = [[0,1],[20,21],[94,95],[0,1]]
    # case = [[69,78],[81,86],]
    # case = [[33,44],[85,95],[20,37],[91,100],[89,100],[77,87],[80,95],[42,61],[40,50],[85,99],[74,91],
    #          [70,82],[5,17],[77,89],[16,26],[21,31],[30,43],[96,100],[27,39],[44,55],[15,34],[85,99],
    #          [74,93],[84,94],[82,94],[46,65],[31,49],[58,73],[86,99],[73,84],[68,80],[5,18],[75,87],
    #          [88,100],[25,41],[66,79],[28,41],[60,70],[62,73],[16,33]]   # 60-70 should be false
    for e in case:
        print(obj.book(e[0], e[1]))