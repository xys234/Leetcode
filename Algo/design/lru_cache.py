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


class LRUCache1:

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


class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Node(value={self.value}, key={self.key})'


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = self.head

    def __str__(self):
        s = ''
        p = self.head.next
        while p:
            s += str(p)
            p = p.next
        return s

    def insert_front(self, value, key):
        if self.head == self.tail:
            self.head.next = Node(value, key)
            self.tail = self.head.next
            self.tail.prev = self.head
            return self.head.next
        else:
            node = Node(value, key)
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            return node

    def remove_tail(self):
        if self.head != self.tail:
            key = self.tail.key
            prev = self.tail.prev
            self.tail = prev
            self.tail.next = None
            return key
        return -1

    def move_to_front(self, node):
        if node:
            if self.head.next != node:
                if node == self.tail:
                    val, key = node.value, node.key
                    self.remove_tail()
                    self.insert_front(val, key)
                else:
                    prev_node = node.prev
                    next_node = node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.seq = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.seq.move_to_front(node)
        print('After get:', self.keys, self.seq)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.seq.move_to_front(node)
        else:
            if len(self.keys) == self.capacity:
                removed_key = self.seq.remove_tail()
                self.keys.pop(removed_key)
            node = self.seq.insert_front(value, key)
            self.keys[key] = node
        print('After put:', self.keys, self.seq)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    capacity = 2
    obj = LRUCache(capacity)

    # case 1
    # obj.put(1, 1)
    # obj.put(2, 2)
    # print(obj.get(1))
    # obj.put(3, 3)
    # print(obj.get(2))
    # obj.put(4, 4)
    # print(obj.get(1))
    # print(obj.get(3))
    # print(obj.get(4))

    # case 2
    # obj.put(2, 1)
    # obj.put(2, 2)
    # print(obj.get(2))
    # obj.put(1, 1)
    # obj.put(4, 1)
    # print(obj.get(2))

    # case 3
    obj.put(2, 1)
    obj.put(1, 1)
    print(obj.get(2))
    obj.put(4, 1)
    print(obj.get(1))
    print(obj.get(2))