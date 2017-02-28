# implement binary search tree with node objects
# implement search, insert, delete binary search tree operations
# implement iterative and recursive binary search tree traversals

class Node(object):
	def __init__(self, data, parent=None):
		self.data = data
		self.parent = None
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree(object):

	def __init__(self, iterable=None):
		self.root = None
		if iterable:
			for item in iterable:
				self.insert(item)

	def preorder_traversal(self, node):
		if node is None:
			return
		print node.data
		self.postorder_traversal(node.leftChild)
		self.postorder_traversal(node.rightChild)

	def inorder_traversal(self, node):
		if node is None:
			return
		self.inorder_traversal(node.leftChild)
		print node.data
		self.inorder_traversal(node.rightChild)

	def postorder_traversal(self, node):
		if node is None:
			return
		self.preorder_traversal(node.leftChild)
		self.preorder_traversal(node.rightChild)
		print node.data
		


	def is_empty(self):
		"""Return True if this binary search tree is empty, or False otherwise"""
		return self.root is None

	def as_sorted_list(self):
		# in order traversal
		# visit left, self, right 
		

		# if it's the third time a node is being accessed, go to parent immediately
		# if current has a left child, step down
		# if current does not have a left child, add self and step up to parent
		# if it is the second time a parent has been traversed over, add it 
		# then go to it's right child 
		# and treat that as current, start again
		pass


	def leafs(self):
		# post order traversal
		# left, right, self
		pass

	def next_steps(self):
		# pre order traversal
		# self, left, right
		pass

	def search(self, data):
		return search_iterative

	def search_recursive(self, data, left=None, right=None):
		pass

	def search_iterative(self, data):
		pass

	def insert(self, data):

		n = Node(data)
		# if bst is empty, create the root
		if self.root is None:
			self.root = n
			return
		
		current = self.root
		while current is not None:
			if data > current.data:
				if current.rightChild is None:
					n.parent = current
					current.rightChild = n
					return
				else: 
					current = current.rightChild
					continue
			elif data < current.data:
				if current.leftChild is None:
					n.parent = current
					current.leftChild = n
					return
				else: 
					current = current.leftChild
					continue
			elif data == current.data:
				raise ValueError, 'item %s already in tree' % data

	def delete(self, data):
		pass


if __name__ == '__main__':
	a = [17, 8, 2]
	bst = BinarySearchTree(a)
	bst.inorder_traversal(bst.root)
	bst.preorder_traversal(bst.root)
	bst.postorder_traversal(bst.root)





