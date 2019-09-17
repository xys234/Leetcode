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
        return f'Node(key={self.key}, value={self.value})'


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def __str__(self):
        s = ''
        p = self.head.next
        while p:
            s += str(p)
            p = p.next
        return s


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.seq = DoublyLinkedList()

    def insert_front(self, value, key):

        node = Node(value, key)
        next_node = self.seq.head.next
        node.next = next_node
        node.prev = self.seq.head

        next_node.prev = node
        self.seq.head.next = node
        self.keys[key] = node

    def remove_node(self, node):
        key = node.key
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev, node.next = None, None
        self.keys.pop(key)

    def move_to_front(self, node):
        if node and self.seq.head.next != self.seq.tail and self.seq.head.next != node:
            k, v = node.key, node.value
            self.remove_node(node)
            self.insert_front(v, k)

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.move_to_front(node)
        print('After get:', self.keys, self.seq)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.move_to_front(node)
        else:
            if len(self.keys) == self.capacity:
                self.remove_node(self.seq.tail.prev)
            self.insert_front(value, key)
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
    obj.put(2, 1)
    obj.put(2, 2)
    print(obj.get(2))
    obj.put(1, 1)
    obj.put(4, 1)
    print(obj.get(2))

    # case 3
    # obj.put(2, 1)
    # obj.put(1, 1)
    # print(obj.get(2))
    # obj.put(4, 1)
    # print(obj.get(1))
    # print(obj.get(2))