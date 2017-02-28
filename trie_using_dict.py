class Trie(object):
	"""todo """
	def __init__(self, iterable=None):
		self.root = {}
		if iterable:
			for item in iterable:
				self.insert(item)

	def insert(self, word):
		current = self.root
		for letter in word:
			if letter in current.keys():
				current = current[letter]
				continue
			else:
				current[letter] = {}
				current = current[letter]
				continue
		# end of word
		current['$'] = '$'

	def contains(self, word):
		current = self.root
		for letter in word:
			if letter in current.keys():
				current = current[letter]
			else:
				return False
		if '$' in current:
			return True
		# if given word is a substring of another word in trie
		else:
			# technically not counted as a word in the trie
			return False

	def delete(self, word):
		if not self.contains(word):
			#  or just return .. 
			raise ValueError, '%s not in trie' % word
		
		current = self.root
		for letter in word:
			# $ won't mess this up bc if there's a $, 
			# this letter is needed for another word in the trie
			#  but if the $ is for the word that's going to be deleted, it'll mess it up
			print len(current.keys())
			print letter
			print current.keys()
			if len(current.keys()) > 1:
				# not safe to delete this level, step down
				current = current[letter]
			else: 
				print 'deletimh'
				print current[letter]
				del current[letter]
				return

	def suggest_completions(self, prefix):
		"""returns all words that begin with given prefix"""
		# prefix has to be at least one character
		assert len(prefix) >= 1
		# step down through entire prefix
		current = self.root
		for letter in prefix:
			try:
				current = current[letter]
			except Exception, e:
				# prefix not in trie
				return "No completions available for %s" % s
		# now at the point in the tree where all possible completions are below 
		print current
		# at this point, can do in order traversal, or can choose a specific num
		#  of completions to return 






if __name__ == '__main__':
	f = open('sample.txt')
	words = f.read().lower().split()
	t = Trie(words)
	print t.contains('tree')
	print t.contains('trie')
	t.suggest_completions('tr')
	t.delete('tree')
	t.suggest_completions('tr')

	







