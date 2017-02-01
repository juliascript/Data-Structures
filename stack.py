#!python
from linkedlist import LinkedList

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        self.data = self.initWithLL()
        # self.data = self.initWithArray()
        self.lengthOfStack = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def initWithArray(self):
        return []

    def initWithLL(self):
        return LinkedList()

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """O(1) Return True if this stack is empty, or False otherwise"""
        return self.lengthOfStack == 0

    def length(self):
        """Return the number of items in this stack"""
        return self.lengthOfStack

    def peek(self):
        """O(1) Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.lengthOfStack == 0:
            return None
        else:
            # return self.data[0]
            return self.data.head.data

    def push(self, item):
        """O(1) Push the given item onto this stack"""
        # self.data.insert(0, item)
        self.data.prepend(item)
        self.lengthOfStack += 1

    def pop(self):
        """O(1) Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.lengthOfStack == 0:
            raise ValueError, 'stack is empty'
        else:
            # top = self.data[0]
            top = self.data.head.data
            # del self.data[0]
            self.data.delete(self.data.head.data)
            self.lengthOfStack -= 1
            return top