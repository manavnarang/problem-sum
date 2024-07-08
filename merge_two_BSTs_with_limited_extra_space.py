# Merge two BSTs using Inbuilt Stack Data structure:
# In this method, we use the inbuilt stack that is present in the STL library so as to get rid of the 
# implementation of the stack part of the code that has been done in the previous implementation.

# Below is the implementation of the above approach.

# Python program to Merge two BSTs with limited extra space

# Structure of a BST Node


class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def mergeTwoBST(root1, root2):
	res = []
	s1, s2 = [], []

	while root1 or root2 or s1 or s2:
		while root1:
			s1.append(root1)
			root1 = root1.left

		while root2:
			s2.append(root2)
			root2 = root2.left

		# Step 3 Case 1:-
		if not s2 or (s1 and s1[-1].val <= s2[-1].val):
			root1 = s1[-1]
			del s1[-1]
			res.append(root1.val)
			root1 = root1.right

		# Step 3 case 2 :-
		else:
			root2 = s2[-1]
			del s2[-1]
			res.append(root2.val)
			root2 = root2.right

	return res


# Driver program to test above functions
if __name__ == '__main__':
	root1 = None
	root2 = None

	''' 
	Let us create the following tree as first tree
			3
			/ \
		1 5
	'''

	root1 = Node(3)
	root1.left = Node(1)
	root1.right = Node(5)

	''' 
	Let us create the following tree as second tree
			4
			/ \
		2 6
	'''

	root2 = Node(4)
	root2.left = Node(2)
	root2.right = Node(6)

	ans = mergeTwoBST(root1, root2)
	for x in ans:
		print(x, end=" ")

# Output
# 1 2 3 4 5 6 
# Time Complexity: O(M+N), M is the size of the first tree and N is the size of the second tree
# Auxiliary Space: O(H1 + H2), H1 is the height of the first tree and H2 is the height of the second tree
