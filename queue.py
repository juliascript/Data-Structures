#!python
from linkedlist import LinkedList

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # self.data = []
        self.data = LinkedList()
        self.lengthOfQueue = 0
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """O(1) Return True if this queue is empty, or False otherwise"""
        return self.lengthOfQueue == 0

    def length(self):
        """O(1) Return the number of items in this queue"""
        return self.lengthOfQueue

    def peek(self):
        """O(1) Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.lengthOfQueue == 0:
            return None
        else: 
            # return self.data[0]
            return self.data.head.data

    def enqueue(self, item):
        """O(1) Enqueue the given item into this queue"""
        self.data.append(item)
        self.lengthOfQueue += 1

    def dequeue(self):
        """O(1) Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.lengthOfQueue == 0:
            raise ValueError, 'queue empty'
        else:
            # first = self.data[0]
            # del self.data[0]
            first = self.data.head.data
            self.data.delete(first)
            self.lengthOfQueue -= 1
            return first
