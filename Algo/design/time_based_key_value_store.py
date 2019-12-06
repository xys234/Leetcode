"""

981.
Medium

"""

import bisect


class ValuePair:
    def __init__(self, t, v):
        self.timestamp = t
        self.value = v

    def __lt__(self, other):
        if self.timestamp < other.timestamp:
            return True
        else:
            return False


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.timemap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key in self.timemap:
            seq = self.timemap[key]
            bisect.insort_left(seq, ValuePair(timestamp, value))
        else:
            seq = []
            bisect.insort_left(seq, ValuePair(timestamp, value))
            self.timemap[key] = seq

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        if key not in self.timemap:
            return None
        else:
            seq = self.timemap[key]
            if timestamp < seq[0].timestamp:
                return None
            else:
                pos = bisect.bisect_left(seq, ValuePair(timestamp, 0))
                if pos == len(seq):
                    return seq[-1].value
                else:
                    if seq[pos].timestamp == timestamp:
                        return seq[pos].value
                    elif seq[pos].timestamp < timestamp:
                        return seq[pos-1].value

obj = TimeMap()
obj.set("foo", "bar", 10)
obj.set("foo", "bar2", 20)
print(obj.get("foo", 3))
print(obj.get("foo", 15))
