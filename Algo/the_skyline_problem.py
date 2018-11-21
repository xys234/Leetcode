class Heap(object):
    def __init__(self):
        self._array = []
        self._last_index = -1

    def push(self, value):
        """
            Append item on the back of the heap,
            sift upwards if heap property is violated.
        """
        self._array.append(value)
        self._last_index += 1
        self._siftup(self.__last_index)

    def pop(self):
        """
            Pop root element from the heap (if possible),
            put last element as new root and sift downwards till
            heap property is satisfied.

        """
        if self._last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self._array[0]
        if self._last_index > 0:  # more than one element in the heap
            self._array[0] = self._array[self._last_index]
            self._siftdown(0)
        self._last_index -= 1
        return root_value

    def peek(self):
        """ peek at the root, without removing it """
        if not self._array:
            return None
        return self._array[0]

    def replace(self, new_value):
        """ remove root & put NEW element as root & sift down -> no need to sift up """
        if self.__ast_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self._array[0]
        self._array[0] = new_value
        self._siftdown(0)
        return root_value

    def heapify(self, input_list):
        """
            each leaf is a trivial subheap, so we may begin to call
            Heapify on each parent of a leaf.  Parents of leaves begin
            at index n/2.  As we go up the tree making subheaps out
            of unordered array elements, we build larger and larger
            heaps, joining them at the i'th element with Heapify,
            until the input list is one big heap.
        """
        n = len(input_list)
        self._array = input_list
        self._last_index = n-1
        for index in reversed(range(n//2)):
            self._siftdown(index)

    @classmethod
    def createHeap(cls, input_list):
        """
            create an heap based on an inputted list.
        """
        heap = cls()
        heap.heapify(input_list)
        return heap

    def _siftdown(self, index):
        current_value = self.__array[index]
        left_child_index, left_child_value = self.__get_left_child(index)
        right_child_index, right_child_value = self.__get_right_child(index)
        # the following works because if the right_child_index is not None, then the left_child
        # is also not None => property of a complete binary tree, else left will be returned.
        best_child_index, best_child_value = (right_child_index, right_child_value) if right_child_index\
        is not None and self.comparer(right_child_value, left_child_value) else (left_child_index, left_child_value)
        if best_child_index is not None and self.comparer(best_child_value, current_value):
            self.__array[index], self.__array[best_child_index] =\
                best_child_value, current_value
            self.__siftdown(best_child_index)
        return


    def _siftup(self, index):
        current_value = self.__array[index]
        parent_index, parent_value = self.__get_parent(index)
        if index > 0 and self.comparer(current_value, parent_value):
            self.__array[parent_index], self.__array[index] = current_value, parent_value
            self.__siftup(parent_index)
        return

    def comparer(self, value1, value2):
        raise NotImplementedError("Should not use the baseclass heap\
            instead use the class MinHeap or MaxHeap.")

    def __get_parent(self, index):
        if index == 0:
            return None, None
        parent_index = (index - 1) // 2
        return parent_index, self.__array[parent_index]

    def __get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__array[left_child_index]

    def __get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.__array[right_child_index]

    def __repr__(self):
        return str(self.__array[:self.__last_index+1])

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.__array == other.__array
        if isinstance(other, list):
            return self.__array == other
        return NotImplemented

class MinHeap(Heap):
    def comparer(self, value1, value2):
        return value1 < value2

class MaxHeap(Heap):
    def comparer(self, value1, value2):
        return value1 > value2


class PriorityQueue(MaxHeap):
    def decrease_key(self, key, new_val):
        pass

    def remove_key(self, key):
        pass

def manualTest():
    """
        Basic test to see step by step changes.
    """
    h = MaxHeap()
    h.push(10)
    assert(h == [10])
    h.push(20)
    assert(h == [20, 10])
    h.push(5)
    assert(h == [20, 10, 5])
    h.push(8)
    assert(h == [20, 10, 5, 8])
    h.push(3)
    assert(h == [20, 10, 5, 8, 3])
    h.push(4)
    assert (h == [20, 10, 5, 8, 3, 4])
    h.push(40)
    assert(h == [40, 10, 20, 8, 3, 4, 5])
    h.push(10)
    assert (h == [40, 10, 20, 10, 3, 4, 5, 8])
    h.push(50)
    assert(h == [50, 40, 20, 10, 3, 4, 5, 8, 10])
    h.push(1)
    assert(h == [50, 40, 20, 10, 3, 4, 5, 8, 10, 1])
    assert(h.pop() == 50)
    assert(h.pop() == 40)
    assert(h.pop() == 20)
    assert(h.pop() == 10)
    assert(h.pop() == 10)
    assert(h.pop() == 8)
    assert(h.pop() == 5)
    assert(h.pop() == 4)
    assert(h.pop() == 3)
    assert(h.pop() == 1)
    try:
        h.pop()
        assert(False)
    except IndexError:  # check if assertion is thrown when heap is empty
        assert(True)
    # check createHeap classmethod.
    assert(MinHeap.createHeap([2,7,3,1,9,44,23]) == [1, 2, 3, 7, 9, 44, 23])
    assert(MaxHeap.createHeap([2,7,3,1,9,44,23]) == [44, 9, 23, 1, 7, 3, 2])



class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

if __name__=='__main__':
    manualTest()