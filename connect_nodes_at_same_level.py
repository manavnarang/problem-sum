# Follow the below steps to Implement the idea:

# Initialize a node pointer Prev to NULL and a queue of node pointer Q.
# Traverse the tree in Breadth-first search order starting from the root.
# Calculate the size sz of the Q and run a for loop from 0 to sz – 1.
# If prev is Null then set prev to the current node.
# Else set prev’s next to the current node and prev to the current node.
# Set prev’s next to Null and prev to Null.
# If the current node’s left is not null push it into the queue.  
# If the current node’s right is not null push it into the queue.
# Below is the Implementation of the above approach:


# Iterative program to connect all the adjacent nodes at the same level in a binary tree
class newnode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = self.nextRight = None

# setting right pointer to next right node

#			 10 ----------> NULL
#			 / \
#		 8 --->2 --------> NULL
#		 /
#		 3 ----------------> NULL


def connect(root):

	# Base condition
	if root is None:
		return

	# Create an empty queue like level order traversal
	queue = []
	queue.append(root)
	while len(queue) != 0:

		# size indicates no. of nodes at current level
		size = len(queue)

		# for keeping track of previous node
		prev = newnode(None)
		for i in range(size):
			temp = queue.pop(0)
			if temp.left:
				queue.append(temp.left)
			if temp.right:
				queue.append(temp.right)
			if prev != None:
				prev.nextRight = temp
				prev = temp
		prev.nextRight = None


# Driver Code
if __name__ == '__main__':

	# Constructed binary tree is
	# 10
	#	 / \
	# 8	 2
	# /
	# 3
	root = newnode(10)
	root.left = newnode(8)
	root.right = newnode(2)
	root.left.left = newnode(3)

	# Populates nextRight pointer in all nodes
	connect(root)

	# Let us check the values of nextRight pointers
	print("Following are populated nextRight",
		"pointers in the tree (-1 is printed",
		"if there is no nextRight)")
	print("nextRight of", root.data, "is ", end="")
	if root.nextRight:
		print(root.nextRight.data)
	else:
		print(-1)
	print("nextRight of", root.left.data, "is ", end="")
	if root.left.nextRight:
		print(root.left.nextRight.data)
	else:
		print(-1)
	print("nextRight of", root.right.data, "is ", end="")
	if root.right.nextRight:
		print(root.right.nextRight.data)
	else:
		print(-1)
	print("nextRight of", root.left.left.data, "is ", end="")
	if root.left.left.nextRight:
		print(root.left.left.nextRight.data)
	else:
		print(-1)
# Output
# Following are populated nextRight pointers in the tree (-1 is printed if there is no nextRight)
# nextRight of 10 is -1
# nextRight of 8 is 2
# nextRight of 2 is -1
# nextRight of 3 is -1
# Time Complexity: O(N)
# Auxiliary Space: O(N)
