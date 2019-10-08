class Node:

	def __init__(self, parent, action, pathcost, state):
		self.parent = parent
		self.action = action
		self.pathcost = pathcost
		self.state = state
	
	def total_path(self):
		states = []
		node = self
		while node.parent != None: 
			states = [node.action] + states
			node = node.parent
		print(states)
		return states


def testpath():
	node = Node(Node(Node(None, None, 0, 0), "North", 10, 1), 'South', 20, 2)
	return node.total_path() == ['North', 'South']

if __name__ == "__main__":
	print(testpath())	
