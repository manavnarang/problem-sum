# Approach: Using Flood-Fill Algorithm and DFS
# This is mainly an application of Flood-Fill algorithm. 
# The main difference here is that a ‘O’ is not replaced by ‘X’ if it lies in region that ends on a boundary. 
# Following are simple steps to do this special flood fill.

# Algorithm:

# 1. Traverse the given matrix and replace all ‘O’ with a special character ‘-‘.
# 2. Traverse four edges of given matrix and call floodFill(‘-‘, ‘O’) for every ‘-‘ on edges. 
# The remaining ‘-‘ are the characters that indicate ‘O’s (in the original matrix) to be replaced by ‘X’.
# 3. Traverse the matrix and replace all ‘-‘s with ‘X’s.

# Python3 program to replace all 'O's with
# 'X's if surrounded by 'X'

# Size of given matrix is M x N
M = 6
N = 6

# A recursive function to replace previous 
# value 'prevV' at '(x, y)' and all surrounding
# values of (x, y) with new value 'newV'.
def floodFillUtil(mat, x, y, prevV, newV):

	# Base Cases
	if (x < 0 or x >= M or y < 0 or y >= N):
		return

	if (mat[x][y] != prevV):
		return

	# Replace the color at (x, y)
	mat[x][y] = newV

	# Recur for north, east, south and west 
	floodFillUtil(mat, x + 1, y, prevV, newV)
	floodFillUtil(mat, x - 1, y, prevV, newV)
	floodFillUtil(mat, x, y + 1, prevV, newV)
	floodFillUtil(mat, x, y - 1, prevV, newV)

# Returns size of maximum size subsquare
# matrix surrounded by 'X'
def replaceSurrounded(mat):

	# Step 1: Replace all 'O's with '-'
	for i in range(M):
		for j in range(N):
			if (mat[i][j] == 'O'):
				mat[i][j] = '-'

	# Call floodFill for all '-' 
	# lying on edges
	# Left Side
	for i in range(M):
		if (mat[i][0] == '-'):
			floodFillUtil(mat, i, 0, '-', 'O')
	
	# Right side
	for i in range(M): 
		if (mat[i][N - 1] == '-'):
			floodFillUtil(mat, i, N - 1, '-', 'O')
	
	# Top side
	for i in range(N): 
		if (mat[0][i] == '-'):
			floodFillUtil(mat, 0, i, '-', 'O')
	
	# Bottom side
	for i in range(N): 
		if (mat[M - 1][i] == '-'):
			floodFillUtil(mat, M - 1, i, '-', 'O')

	# Step 3: Replace all '-' with 'X'
	for i in range(M):
		for j in range(N):
			if (mat[i][j] == '-'):
				mat[i][j] = 'X'

# Driver code
if __name__ == '__main__':

	mat = [ [ 'X', 'O', 'X', 'O', 'X', 'X' ], 
			[ 'X', 'O', 'X', 'X', 'O', 'X' ], 
			[ 'X', 'X', 'X', 'O', 'X', 'X' ], 
			[ 'O', 'X', 'X', 'X', 'X', 'X' ], 
			[ 'X', 'X', 'X', 'O', 'X', 'O' ], 
			[ 'O', 'O', 'X', 'O', 'O', 'O' ] ]; 

	replaceSurrounded(mat)

	for i in range(M):
		print(*mat[i])
# Output
# X O X O X X 
# X O X X X X 
# X X X X X X 
# O X X X X X 
# X X X O X O 
# O O X O O O 
# Time Complexity: O(MN). Note that every element of matrix is processed at most three times.
# Auxiliary Space: O(M x N), as implicit stack is used due to recursive call
