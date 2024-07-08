# [Method 2 ]( Efficient solution )
#  An Efficient solution based on tree serialization and hashing. 
# The idea is to serialize subtrees as strings and store the strings in hash table. 
# Once we find a serialized tree (which is not a leaf) already existing in hash-table, we return true. 

# Below The implementation of above idea. 

# Python program to find if there is a duplicate
# sub-tree of size 2 or more.

# A binary tree node has data,
# pointer to left child and a
# pointer to right child


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSame(T, S):
    if T is None and S is None:
        return True
    if T is None or S is None:
        return False
    if T.data == S.data and isSame(T.left, S.left) and isSame(T.right, S.right):
        return True
    return False


def isSubtree(T, S):
    if T is None or S is None:
        return False
    if T == S:
        return False
    return isSame(T, S) or isSubtree(T.left, S) or isSubtree(T.right, S)


def findDuplicates(T, S):
    if T is None or S is None:
        return False
    if S.left is None and S.right is None:
        return False
    if T != S:
        if isSubtree(T, S):
            return True
    left = findDuplicates(T, S.left)
    if left:
        return True
    right = findDuplicates(T, S.right)
    return right


def dupSub(root):
    if root is None:
        return 0
    return 1 if findDuplicates(root, root) else 0


# Driver code
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('B')
root.right.right.right = Node('E')
root.right.right.left = Node('D')

if dupSub(root):
    print("Yes")
else:
    print("No")
# Output
#  Yes 
# Time Complexity: O(n)
# Auxiliary Space: O(n)
