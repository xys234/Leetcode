

from collections import namedtuple

BaseNetworkRecord = namedtuple('BaseNetworkRecord', ('ANode', 'BNode'))

class Record:

    fmt_binary = None
    fmt_string = None

    def __init__(self, values):
        self.values = values

    def to_string(self):
        print('to_string called')

    def to_binary(self):
        print('to_binary called')

    def convert(self):
        pass

    def from_string(self):
        pass

class NetworkRecord(Record, BaseNetworkRecord):
    Record.fmt_string = 'i'
    Record.fmt_binary = 'i'



