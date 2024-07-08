# Optimal Strategy for a Game using dp:
# To solve the problem follow the below idea:

# Since the same subproblems are called again, this problem has the Overlapping Subproblems property. 
# So the re-computations of the same subproblems can be avoided by 
# constructing a temporary array in a bottom-up manner using the above recursive formula.

# Follow the below steps to solve the problem:

# 1. Create a 2-D array table of size N * N
# 2. Run a nested for loop to consider i and j at every possible position with a distance equal to ‘gap’ between them
#     a. Declare an integer x, If (i+2) is less than or equal to j then set x equal to table[i+2][j], else equal to zero
#     b. Declare an integer y, If (i+1) is less than or equal to j-1 then set y equal to table[i+1][j-1], else equal to zero
#     c. Declare an integer z, If i is less than or equal to j-2 then set z equal to table[i][j-2], else equal to zero
#     d. Set table[i][j] equal to maximum of arr[i] + min(x, y) or arr[j] + min(y, z)
# 3. Return table[0][N-1]
# Below is the implementation of the above approach:

# Python3 program to find out maximum
# value from a given sequence of coins

# Returns optimal value possible that
# a player can collect from an array
# of coins of size n. Note than n
# must be even


def optimalStrategyOfGame(arr, n):

	# Create a table to store
	# solutions of subproblems
	table = [[0 for i in range(n)]
			for i in range(n)]

	# Fill table using above recursive
	# formula. Note that the table is
	# filled in diagonal fashion
	# from diagonal elements to
	# table[0][n-1] which is the result.
	for gap in range(n):
		for j in range(gap, n):
			i = j - gap

			# Here x is value of F(i + 2, j),
			# y is F(i + 1, j-1) and z is
			# F(i, j-2) in above recursive
			# formula
			x = 0
			if((i + 2) <= j):
				x = table[i + 2][j]
			y = 0
			if((i + 1) <= (j - 1)):
				y = table[i + 1][j - 1]
			z = 0
			if(i <= (j - 2)):
				z = table[i][j - 2]
			table[i][j] = max(arr[i] + min(x, y),
							arr[j] + min(y, z))
	return table[0][n - 1]


# Driver Code
arr1 = [8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))

arr2 = [2, 2, 2, 2]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))

arr3 = [20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))

# Output
# 22
# 4
# 42

# Time Complexity: O(N2). 
# Auxiliary Space: O(N2). As a 2-D table is used for storing states.

# Note: The above solution can be optimized by using less number of comparisons for every choice.
