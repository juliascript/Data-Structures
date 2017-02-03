import random
from linkedlist import LinkedList

class Hashtable(object):
	def __init__(self):
		self.buckets = [LinkedList() for i in range(5)]
		# self.length = 0

	def append(self, obj):
		# O(3n)
		# if obj is not already in set, 
		index = hash(obj) % len(self.buckets)
		for node in self.buckets[index]:
			if node == obj:
				return
		# if ll is longer than 5 items, resize and recalculate index
		if self.buckets[index].length() > 5:
			self.resize()
			index = hash(obj) % len(self.buckets)
		# add it to its linked list 
		self.buckets[index].append(obj)
		# self.length += 1

	def remove(self, obj):
		# O(len(ll))
		# find index of obj in hash table
		index = hash(obj) % len(self.buckets)
		# remove it from ll
		self.buckets[index].delete(obj)
		# self.length -= 1

	def items(self):
		# O(n)
		allItems = []
		for ll in self.buckets:
			for node in ll:
				allItems.append(node)
		return allItems

	def resize(self):
		print "resizing"
		# O(2n)
		items = self.items()
		newSize = len(self.buckets) * 2
		self.buckets = [LinkedList() for i in range(newSize)]
		for item in items:
			index = hash(item) % newSize
			self.buckets[index].append(item)

if __name__ == "__main__":
	h = Hashtable()
	h.append('hi')
	h.append('hello')
	h.append('hello')
	print h.items()
	print len(h.buckets)
	for i in range(2000):
		string = 'h%d' % random.randint(1, 90)
		h.append(string)
	print len(h.buckets)