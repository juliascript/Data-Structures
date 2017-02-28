import random

class Node(object):
	def __init__(self, data):
		self.data = data
		self.adjacent_nodes = [] 

class Graph(object):
	def __init__(self, iterable=None):
		self.edges = [] # list of tuples
		self.nodes = [] # list of nodes
		if iterable:
			for item in iterable:
				self.insert(item)

	def insert(self, data):
		n = Node(data)
		# add it to nodes list on graph class
		self.nodes.append(n)
		# -- if no connection is specified, add it as a standalone node (but how would that be searched?)

	def add_edge(self, n1, n2):
		# create tuple for n1, n2 
		edge = (n1, n2)
		# add to edges list on graph class
		self.edges.append(edge)

		# add n1 to adjacent_nodes of n2 list on node class
		n2.adjacent_nodes.append(n1)
		# add n2 to adjacent_nodes of n1 list on node class
		n1.adjacent_nodes.append(n2)

	def depth_first_search(self, item, current_node=None, visited_dict = None):
		# if first call in stack, pick a random node and walk around
		if current_node is None:
			current_node = random.choice(self.nodes)
			visited_dict = {}

		eligible_nodes = []

		# filter out all adjacent nodes that haven't been visited
		for node in current_node.adjacent_nodes:
			if node not in visited_dict:
				eligible_nodes.append(node)
		# if empty, return not found 
		if eligible_nodes == []:
			return False
			# return "%s not found in graph" % item

		# if equal to item, return true/node
		if item in eligible_nodes:
			return True
			# should probably return somethign else

		# find lowest element and step down and recursively call this function
		if len(eligible_nodes) == 2:
			if eligible_nodes[0] < eligible_nodes[1]:
				visited_dict[eligible_nodes[0]] = True
				return depth_first_search(item, eligible_nodes[0], visited_dict)
			else:
				visited_dict[eligible_nodes[1]] = True
				return depth_first_search(item, eligible_nodes[1], visited_dict)
		else: 
			# sort and find lowest, then call recursively
			pass

	def breadth_first_search(self, item, current_node=None, visited_dict=None):
		# if first call in stack, pick a random node and walk around
		if current_node is None:
			current_node = random.choice(self.nodes)
			visited_dict = {}

		eligible_nodes = []

		# filter out all adjacent nodes that haven't been visited
		for node in current_node.adjacent_nodes:
			if node not in visited_dict:
				eligible_nodes.append(node)

		# if empty, return not found
		if eligible_nodes == []:
			return False
			# return "%s not found in graph" % item

		# if equal to item, return true/node
		if item in eligible_nodes:
			return True
			# should probably return somethign else

		# call this function recursively for each node
		for node in eligible_nodes:
			visited_dict[node] = True
			return breadth_first_search(item, node, visited_dict)

def main():
	g = Graph()

if __name__ == "__main__":
	main()