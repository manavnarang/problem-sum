# The idea is to do a preorder traversal of the tree. 
# In the preorder traversal, keep track of the value calculated till the current node, let this value be val. 
# For every node, we update the val as val*10 plus the node’s data. 

# Python program to find sum of all paths from root to leaves

# A Binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Returns sums of all root to leaf paths. The first parameter is root
# of current subtree, the second paramete"r is value of the number
# formed by nodes from root to this node
def treePathsSumUtil(root, val):

	# Base Case
	if root is None:
		return 0

	# Update val
	val = (val*10 + root.data)

	# If current node is leaf, return the current value of val
	if root.left is None and root.right is None:
		return val

	# Recur sum of values for left and right subtree
	return (treePathsSumUtil(root.left, val) +
			treePathsSumUtil(root.right, val))

# A wrapper function over treePathSumUtil()
def treePathsSum(root):
	
	# Pass the initial value as 0 as there is nothing above root
	return treePathsSumUtil(root, 0)

# Driver function to test above function
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print ("Sum of all paths is", treePathsSum(root))

# Output
# Sum of all paths is 13997
# Time Complexity: The above code is a simple preorder traversal code that visits every node exactly once. Therefore, the time complexity is O(n) where n is the number of nodes in the given binary tree.
# Auxiliary Space: O(n)
