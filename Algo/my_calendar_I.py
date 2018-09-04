""""

729. My Calendar I

Implement a MyCalendar class to store your events.
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection
(ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully
without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].


"""


class MyCalendar:

    def __init__(self):
        self.calendar = []              # use an array sorted by event start time

    def search(self, event):
        """
        find the insertion point, the event time earlier and closest to start_time
        :param t: (start_time, end_time)
        :return:
        """

        if not self.calendar:
            self.calendar.append(event)
        else:
            head = 0
            tail = len(self.calendar)
            while tail - head > 1:
                if self.calendar[(tail+head)//2][0] > event[0]:
                    tail = (tail+head)//2
                elif self.calendar[(tail+head)//2][0] < event[0]:
                    head = (tail+head)//2
                else:
                    return (tail+head)//2 - 1
            return head

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if not self.calendar:
            return True
        else:
            nearest_index = self.search((start, end))
            left_check, right_check = True, True
            i = nearest_index
            while self.calendar[i][1] > start and left_check and i >= 0:
                pass
            i = nearest_index + 1
            while self.calendar[i][0] < end and right_check and i < len(self.calendar):
                pass

        if left_check and right_check:
            pass
            # insert and return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


if __name__ == '__main__':

    obj = MyCalendar()
    seq = [1,3,4,6,7,8,10,13]
    seq = [(i, 1) for i in seq ]
    obj.calendar = seq
    print(obj.search((5,14)))