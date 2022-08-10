def isEven(value):
    return value & 1 == 0


class CyclesQueueListItem:
    def __init__(self, next_element=None):
        self._data = 0
        self._next_element = next_element

    def next_element(self):
        return self._next_element

    def set_next_element(self, next_element):
        self._next_element = next_element

    def data(self):
        return self._data

    def set_data(self, data):
        self._data = data


class CyclesQueueList:
    def __init__(self, size):
        self._size = size
        self._count = 0

        temp = CyclesQueueListItem()
        first = temp

        for i in range(size - 1):
            temp = CyclesQueueListItem(temp)

        first.set_next_element(temp)

        self._head = first
        self._tail = first

    def size(self):
        return self._size

    def count(self):
        return self._count

    def empty(self):
        return self._count == 0

    def full(self):
        return self._count == self._size

    def push(self, el):
        if self.full():
            raise Exception("Queue is full!")

        self._head.set_data(el)
        self._count += 1
        self._head = self._head.next_element()

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty!")

        item = self._tail.data()

        self._count -= 1

        self._tail = self._tail.next_element()
        return item


class CyclesQueue:
    def __init__(self, size):
        self._items = [0] * size
        self._head = 0
        self._tail = 0

        self._count = 0
        self._size = size

    def push(self, el):
        if self.full():
            raise Exception("Queue is full!")

        self._items[self._head] = el

        self._count += 1
        self._head = self.next_index(self._head)

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty!")

        item = self._items[self._tail]

        self._count -= 1

        self._tail = self.next_index(self._tail)
        return item

    def count(self):
        return self._count

    def size(self):
        return self._size

    def full(self):
        return self._count == self._size

    def empty(self):
        return self._count == 0

    def next_index(self, index):
        temp = index + 1
        if temp >= self._size:
            temp = 0
        return temp
