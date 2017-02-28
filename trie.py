# this in in data structures directory

class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = []
		self.data.append(data)
		self.children = []
		self.suggestions = []

class Trie(object):
	"""docstring for Trie"""
	def __init__(self, iterable=None):
		self.root = []
		if iterable:
			for item in iterable:
				self.insert(item)

	def insert(self, data):
		# this is wrong -- each letter should have it's own node
		n = Node(data)
		if self.root is None:
			self.root.append(n)
			return

		current = self.root 
		for letter in data:
			if letter not in self.root:
				self.root.append(n)
				self._insert_helper(data)
			else:
				index = self.root.index(letter)
				current = self.root[index]
				self._insert_helper(data)


	def _insert_helper(self, data):
		pass

	def suggest(self, prefix):
		for letter in prefix:
			try:
				# traverse down the tree to the node that is 
				# the last character given 
				if letter in current.data:
					index = current.data.index(letter)
					current = current.data[index]
				pass
			except Exception, e:
				# the string provided did not match anything 
				# currently in the trie
				return "No suggestions available for %s" % string
		# now any completions from here qualify 
		# in order traversal but keeping track of the current prefix 
		# probably will have to change iteration above to incorporate 
		#  recursion 








		
