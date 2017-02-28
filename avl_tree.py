class Node(object):
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left_child = None
		self.right_child = None
		self.height = 0

class AVLTree(object):
	def __init__(self, iterable=None):
		self.root = None
		if iterable:
			for item in iterable:
				self.insert(item)

	def update_height(self, node=None):
		# traverse the tree and update heights starting at leaves
		# this updates the height from the current node (to root)
		if node is None:
			return

		if node.left_child is None and node.right_child is None:
			node.height = 0
		elif node.left_child is None and node.right_child is not None:
			node.height = node.right_child.height + 1
		elif node.right_child is None and node.left_child is not None:
			node.height = node.left_child.height + 1
		else:
			node.height = max(node.left_child.height, node.right_child.height) + 1
		
		if node.parent is not None:
			update_height(node.parent)
		else:
			return

	def current_balance(self, node):
		return node.left_child.height - node.right_child.height

	def left_rotate(self, node):
		print 'left rotate'
		# node's parent becomes its left child
		current_parent = node.parent
		parent_to_be = node
		current_parent.parent = parent_to_be
		# but what about when node has a left child?
		parent_to_be.left_child = current_parent
		# update height of entire tree
		update_height()


	def right_rotate(self, node):
		print 'right rotate'
		# node's parent becomes its right child
		current_parent = node.parent
		parent_to_be = node
		current_parent.parent = parent_to_be
		parent_to_be.right_child = current_parent
		# update height of entire tree
		update_height()

	def insert(self, data):
		n = Node(data)

		if self.root is None:
			self.root = n
			return

		current = self.root
		while current is not None:
			if data < current.data:
				if current.left_child is None:
					# insert at left child
					n.parent = current
					n.height = 0
					current.left_child = n
					self.update_height(current)
					continue
				else:
					current = current.left_child
					continue
			elif data > current.data:
				n.parent = current
				n.height = 0
				current = current.right_child
				self.update_height(current)
				continue
			elif data == current.data:
				raise ValueError, '%s already in bst' % data
		
		# check for balance as you're walking up the tree
		current_node = current
		while current_node is not None:
			bal = self.current_balance(current_node)
			if bal > 1:
				if current.left_child.height > current.right_child.height:
					# left left
					current = self.right_rotate(current)
				else: 
					# left right
					current.left_child = self.left_rotate(current.left_child)
					current = self.right_rotate(current)
			elif bal < -1:
				if current.right_child.height > current.left_child.height:
					# right right
					current = self.left_rotate(current)
				else:
					# right left
					current.right_child = self.right_rotate(current.right_rotate)
					current = self.left_rotate(current)
			else: 
				return
			current_node = current_node.parent

if __name__ == "__main__":
	arr = [10, 5, 6, 7, 8, 9, 11]
	avl = AVLTree(arr)



