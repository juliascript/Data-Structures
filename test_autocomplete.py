from trie_using_dict import Trie
import unittest

class TrieTest(unittest.TestCase):

	def test_init(self):
		t = Trie()
		assert self.root == {}

	def test_insert(self):
		t = Trie()
		t.insert('this')
		assert 't' in self.root
		assert 'h' in self.root['t']
		assert 'i' in self.root['t']['h']
		assert 's' in self.root['t']['h']['i']
		
	def test_insert_overlap(self):
		t = Trie()
		t.insert('this')
		t.insert('that')
		assert 't' in self.root
		assert 'h' in self.root['t']
		assert 'a' in self.root['t']['h']
		assert 't' in self.root['t']['h']['a']
		assert 'i' in self.root['t']['h']
		assert 's' in self.root['t']['h']['i']

	def test_insert_duplicate_object(self):
		pass

	def test_search(self):
		pass

	def test_delete(self):
		pass

	def test_delete_object_not_in_trie(self):
		pass