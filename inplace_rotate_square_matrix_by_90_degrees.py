# Algorithmic steps for implementation –
# the algorithmic steps to in-place rotate a square matrix by 90 degrees:
# Transpose the matrix: For each element matrix[i][j] where i < j, swap it with the element matrix[j][i].
# Reverse each row of the matrix: For each row i of the matrix, reverse the order of the elements by swapping matrix[i][j] with matrix[i][n – j – 1] where n is the number of columns in the matrix.
# The matrix is now rotated by 90 degrees in place.
# Note: The first step transforms the matrix into its transposed form, and the second step reverses the elements in each row, resulting in a rotation of the matrix by 90 degrees.

# Python program for the above approach
def rotateMatrix(matrix):
	n = len(matrix)
	
	# transpose the matrix
	for i in range(n):
		for j in range(i,n):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
		
	# reverse each column
	for i in range(n):
		for j in range (int(n/2)):
			temp = matrix[n-j-1][i]
			matrix[n-j-1][i] = matrix[j][i]
			matrix[j][i] = temp
		
# driver program
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateMatrix(matrix)
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		print(matrix[i][j], end=" ")
	print("")

# Output
# 3 6 9 
# 2 5 8 
# 1 4 7 
# Explanation –
# In this implementation, the rotateMatrix function takes a 2D vector matrix as input and rotates the matrix by 90 degrees in the anticlockwise direction in place.
# The first step is to transpose the matrix, which is done by swapping the elements matrix[i][j] and matrix[j][i] for i < j.
# The second step is to reverse each column of the matrix, which is done by swapping the elements matrix[j][i] and matrix[n – j – 1][i] where n is the number of rows in the matrix.
# The time complexity of this algorithm is O(n^2), where n is the number of rows (and columns) in the matrix. This is because the algorithm performs a constant amount of work for each element in the matrix.
# The Auxiliary Space needed for this algorithm is O(1), since no extra space is used.
