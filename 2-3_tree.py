class Node(object):
	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None
		self.middle_child = None

class Tree(object):
	def __init__(self, iterable=None):
		self.root = None
		if iterable:
			for item in iterable:
				self.insert(item)

	def insert(self, data):
		n = Node(data)

		if self.root is None:
			self.root = n
			return 

		current = self.root
		while current is not None: 
			if current.data > data:
				# go left
			elif current.data < data:
				# go right
