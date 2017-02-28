#!python

from binary_search_tree import BinarySearchTree, Node
import unittest

class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.leftChild is None
        assert node.rightChild is None

class BinarySearchTreeTest(unittest.TestCase):

    def test_init(self):
        bst = BinarySearchTree()
        assert bst.root is None
        assert bst.is_empty() is True

    def test_init_with_list(self):
        bst = BinarySearchTree(['A', 'B', 'C'])
        assert bst.root.data == 'A'
        assert bst.root.rightChild.data == 'B'
        assert bst.is_empty() is False

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert('A')
        assert bst.root.data == 'A'
        assert bst.root.leftChild == None
        assert bst.root.rightChild == None
        bst.insert('B')
        assert bst.root.data == 'A'
        assert bst.root.leftChild == None
        assert bst.root.rightChild.data == 'B'
        bst.insert('C')
        assert bst.root.data == 'A'
        assert bst.root.leftChild == None
        assert bst.root.rightChild.rightChild.data == 'C'

    def disabled_test_delete(self):
        ll = LinkedList(['A', 'B', 'C'])
        ll.delete('A')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        ll.delete('C')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'B'
        ll.delete('B')
        assert ll.head is None
        assert ll.tail is None
        with self.assertRaises(ValueError):
            ll.delete('D')

    def disabled_test_find(self):
        ll = LinkedList(['A', 'B', 'C'])
        assert ll.find(lambda item: item == 'B') == 'B'
        assert ll.find(lambda item: item < 'B') == 'A'
        assert ll.find(lambda item: item > 'B') == 'C'
        assert ll.find(lambda item: item == 'D') is None


if __name__ == '__main__':
    unittest.main()
