class Queue(object):
    """队列 FIFO（first in first out）"""
    def __init__ (self):
        self._list = []
    def enqueue(self, item):
        self._list.append(item)
    def dequeue(self, item):
        return self._list.pop(0)
    def is_empty(self):
        return self._list == []
    def size(self):
        return len(self._list)
class Doublequeue(object):
    def __init__(self):
        self._list = []
    def add_front(self, item):
        self._list.insert(0,item)
    def add_rear(self, item):
        self._list.append(item)
    def pop_front(self, item):
        self._list.pop(0)
    def pop_rear(self, item):
        self._list.pop()
    def is_empty(self):
        return self._list == []
    def size(self):
        return len(self._list)       
    