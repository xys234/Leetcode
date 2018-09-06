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

class MyCalendar:

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
            left_check, right_check = True, True

            i = nearest_index
            while left_check and i > 0:
                violations = 0

                if self.calendar[i-1][1] > start:
                    left_check = False
                else:
                    break
                i -= 1

            i = nearest_index
            while right_check and i < len(self.calendar):
                if self.calendar[i][0] < end or i < 0:
                    right_check = False
                else:
                    break
                i += 1



        if left_check and right_check:
            # insert and return True
            left = self.calendar[:nearest_index]
            right = self.calendar[nearest_index:]
            self.calendar = left + [(start, end)] + right
            return True
        else:
            return False


if __name__ == '__main__':

    obj = MyCalendar()
    case = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    # case = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    for e in case:
        print(obj.book(e[0], e[1]))