# x implement set with hash table
# x implement automatic resizing of hash table
# x annotate functions with complexity analysis
# stretch: implement set operations union, intersection, difference, subset
# stretch: implement circular buffer with dynamic array and linked list

import random
from hashtable import Hashtable

class Set(object):
	def __init__(self):
		self.length = 0
		self.hashtable = Hashtable()

	def length(self):
		# O(1)
		return self.length

	def append(self, obj):
		# O(3n)
		self.hashtable.append(obj)
		self.length += 1

	def remove(self, obj):
		# O(len(ll))
		self.hashtable.remove(obj)
		self.length -= 1

	def items(self):
		# O(n)
		return self.hashtable.items()

if __name__ == "__main__":
	s = Set()
	s.append('hi')
	s.append('hello')
	s.append('hello')
	print s.items()
	for i in range(2000):
		string = 'h%d' % random.randint(1, 90)
		s.append(string)