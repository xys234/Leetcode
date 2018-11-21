

from enum import IntEnum


class EventType(IntEnum):
    ENTER = 1
    LEAVING = -1


class Event:
    eid = -1
    def __init__(self, h, type):
        Event.eid += 1
        self._id = Event.eid
        self._height = h
        self._type = type

    def __lt__(self, other):
        return self._height * self._type > other._height * other._type

    def __repr__(self):
        return "event(%d, %d)" % (self._height, self._type)


if __name__=='__main__':
    l = [Event(3, EventType.ENTER), Event(4, EventType.ENTER), Event(3, EventType.LEAVING)]
    print(sorted(l))
