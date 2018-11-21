"""

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively,
and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ]
that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment.
Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline,
and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[[2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

"""

from enum import IntEnum


class EventType(IntEnum):
    ENTER = 1
    LEAVING = -1


class Event:
    eid = -1
    def __init__(self, x, h, type):
        Event.eid += 1
        self._id = Event.eid
        self._x = x
        self._height = h
        self._type = type

    def __lt__(self, other):
        if self._x == other._x:
            return self._height * self._type > other._height * other._type
        else:
            return self._x < other._x

    def __str__(self):
        return "event(id=%d, x=%d, h=%d, type=%d)" % (self._id, self._x, self._height, self._type)


class MaxHeap:
    def __init__(self, maxsize):
        self._vals = [()]*maxsize       # (height, id)
        self._idx = [0]*maxsize       # idx_[id] is the index of the element in the heap, i,e, vals
        self._size = 0

    def add(self, e):
        """
        :param e:
        :type Event
        :return:
        """
        self._idx[e._id] = self._size
        self._vals[self._size] = (e._height, e._id)
        self._size += 1

    def _swap_nodes(self, i, j):
        self._idx[self._vals[i][1]], self._idx[self._vals[j][1]] = \
            self._idx[self._vals[j][1]], self._idx[self._vals[i][1]]
        self._vals[i], self._vals[j] = self._vals[j], self._vals[i]

    def max_heapify_up(self, i):
        """
        Heapify by sifting up the element
        :param i: the ith element of the heap
        :return:
        """
        p = (i-1) // 2
        if self._vals[p][0] > self._vals[i][0] or i == 0:
            return
        else:
            self._swap_nodes(p, i)
            self.max_heapify_up(p)

    def max_heapify_down(self, i):
        c1, c2 = 2*i+1, 2*i+2
        if c1>=self._size:
            return
        else:
            while True:
                if self._vals[c1][0] > self._vals[c2][0]:
                    max_c = c1
                else:
                    max_c = c2
                self._swap_nodes(max_c, i)
                self.max_heapify_down(max_c)

    def remove_max(self):
        self._swap_nodes(0, self._size-1)
        self._vals.pop()
        self._idx.pop()
        self._size -= 1
        self.max_heapify_down(0)

    def remove_by_id(self, eid):
        index = self._idx[eid]
        self._swap_nodes(index, self._size-1)
        self._vals.pop()
        self._idx.pop()
        self._size -= 1

    def empty(self):
        return self._size == 0

    def max(self):
        if self.empty():
            return 0        # specific to this implementation. heights are always positive
        else:
            return self._vals[0][0]


class Solution:
    @classmethod
    def get_events(cls, buildings):
        """
        Convert buildings to entering and leaving events
        :param buildings: [(start_x, end_x, height)]
        :type list
        :return:
        """
        events = []
        for b in buildings:
            events.append(Event(b[0], b[2], EventType.ENTER))
            events.append(Event(b[1], b[2], EventType.LEAVING))
        events = sorted(events)
        return events


    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = self.get_events(buildings)
        number_of_events = len(events)
        heap = MaxHeap(number_of_events)

        skyline = []
        for e in events:
                x = e._x
                h = e._height
                id = e._id
                type = e._type
                if type == EventType.ENTER:
                    if heap.empty() or h > heap.max():
                        heap.add(e)
                        skyline.append((x, h))
                else:
                    heap.remove_by_id(id)
                    if h > heap.max():
                        skyline.append((x, h))
        return skyline




if __name__=='__main__':
    buildings = [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
    print(list(map(str,Solution.get_events(buildings))))