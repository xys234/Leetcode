"""

146. LRU Cache

Medium


"""


class ListNode:
    def __init__(self, val=-1, key=None):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

    def __repr__(self):
        return self.__class__.__name__ + '(key={key}, val={val})'.format(key=self.key, val=self.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = {}  # key to ListNode map
        self.head = ListNode()  # list store actual data to support fast push
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.index:
            node = self.index[key]
            self.moveNodeToTop(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.index:
            node = self.index[key]
            node.val = value
        else:
            new_node = ListNode(value, key)
            self.addNodeToTop(new_node)
            self.index[key] = new_node

            if self.capacity < len(self.index):

                removed_node = self.removeLeastUsedNode()
                self.index.pop(removed_node.key)

    def addNodeToTop(self, node):
        '''
        Adding new node in the fron of the cache, latest accessed by client
        '''
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        '''
        Remove node from the list from any place
        '''
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def moveNodeToTop(self, node):
        '''
        Move the latest accessed node to be in the beginning of the cache
        '''
        self.removeNode(node)
        self.addNodeToTop(node)

    def removeLeastUsedNode(self):
        '''
        Use this function to remove the least recently used node
        '''
        node = self.tail.prev
        self.removeNode(node)
        return node


if __name__ == '__main__':
    capacity = 2
    obj = LRUCache(capacity)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))