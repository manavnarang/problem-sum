# Dynamic Programming: 

# Let the given set of vertices be {1, 2, 3, 4,….n}. Let us consider 1 as starting and ending point of output. For every other vertex I (other than 1), we find the minimum cost path with 1 as the starting point, I as the ending point, and all vertices appearing exactly once. Let the cost of this path cost (i), and the cost of the corresponding Cycle would cost (i) + dist(i, 1) where dist(i, 1) is the distance from I to 1. Finally, we return the minimum of all [cost(i) + dist(i, 1)] values. This looks simple so far. 

# Now the question is how to get cost(i)? To calculate the cost(i) using Dynamic Programming, we need to have some recursive relation in terms of sub-problems. 

# Let us define a term C(S, i) be the cost of the minimum cost path visiting each vertex in set S exactly once, starting at 1 and ending at i. We start with all subsets of size 2 and calculate C(S, i) for all subsets where S is the subset, then we calculate C(S, i) for all subsets S of size 3 and so on. Note that 1 must be present in every subset.

# If size of S is 2, then S must be {1, i},
#  C(S, i) = dist(1, i) 
# Else if size of S is greater than 2.
#  C(S, i) = min { C(S-{i}, j) + dis(j, i)} where j belongs to S, j != i and j != 1.
# Below is the dynamic programming solution for the problem using top down recursive+memoized approach:-

# For maintaining the subsets we can use the bitmasks to represent the remaining nodes in our subset. Since bits are faster to operate and there are only few nodes in graph, bitmasks is better to use.

# For example: –  

# 10100 represents node 2 and node 4 are left in set to be processed

# 010010 represents node 1 and 4 are left in subset.

# NOTE:- ignore the 0th bit since our graph is 1-based

n = 4 # there are four nodes in example graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using 
# all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
	0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
	# base case
	# if only ith bit and 1st bit is set in our mask,
	# it implies we have visited all other nodes already
	if mask == ((1 << i) | 3):
		return dist[1][i]

	# memoization
	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 10**9 # result of this sub-problem

	# we have to travel all nodes j in mask and end the path at ith node
	# so for every node j in mask, recursively calculate cost of 
	# travelling all nodes in mask
	# except i and then travel back from node j to node i taking 
	# the shortest path take the minimum of all possible j nodes
	for j in range(1, n+1):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
	memo[i][mask] = res # storing the minimum value
	return res


# Driver program to test above logic
ans = 10**9
for i in range(1, n+1):
	# try to go from node 1 visiting all nodes in between to i
	# then return from i taking the shortest route to 1
	ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])

print("The cost of most efficient tour = " + str(ans))

# Output
# The cost of most efficient tour = 80
# Time Complexity : O(n2*2n) where O(n* 2n) are maximum number of unique subproblems/states and O(n) for transition (through for loop as in code) in every states.

# Auxiliary Space: O(n*2n), where n is number of Nodes/Cities here.
