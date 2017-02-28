from avl_tree import AVLTree
import unittest

class AVLTreeTest(unittest.TestCase):

	# def setup(self):
	# 	avl = AVLTree()

	# def teardown(self):
	# 	pass

	def test_init(self):
		avl = AVLTree()
		assert avl.root is None

	def test_insert_with_one_value(self):
		avl = AVLTree()
		avl.insert(4)
		assert avl.root.data == 4
		assert avl.root.right_child is None
		assert avl.root.left_child is None

	def test_insert_with_two_values(self):
		avl = AVLTree()
		avl.insert(4)
		avl.insert(9)
		assert avl.root.data == 4
		assert avl.root.right_child.data == 9
		assert avl.root.left_child is None

	def test_insert_duplicate_value(self):
		# expect a ValueError to be raised
		pass

	def test_right_rotation(self):
		avl = AVLTree()
		avl.insert(0)
		avl.insert(1)
		avl.insert(2)
		assert avl.root.data == 1
		assert avl.root.left_child.data == 0
		assert avl.root.right_child.data == 2

	def test_left_rotation(self):
		avl = AVLTree()
		avl.insert(2)
		avl.insert(1)
		avl.insert(0)
		assert avl.root.data == 1
		assert avl.root.left_child.data == 0
		assert avl.root.right_child.data == 2

	def test_right_right_rotation(self):
		avl = AVLTree()
		avl.insert(0)
		avl.insert(1)
		avl.insert(2)
		avl.insert(3)
		avl.insert(4)
		avl.insert(5)
		assert avl.root.data == 2
		assert avl.root.left_child.data == 1
		# ?
		assert avl.root.right_child.data == 4

	def test_right_left_rotation(self):
		pass

	def test_left_left_rotation(self):
		avl = AVLTree()
		avl.insert(5)
		avl.insert(4)
		avl.insert(3)
		avl.insert(2)
		avl.insert(1)
		avl.insert(0)
		assert avl.root.data == 2
		assert avl.root.left_child.data == 1
		# ?
		assert avl.root.right_child.data == 4

	def test_left_right_rotation(self):
		pass

	def test_remove_leaf(self):
		pass

	def test_remove_path_node(self):
		pass

	def test_search(self):
		pass


if __name__ == '__main__':
	unittest.main()