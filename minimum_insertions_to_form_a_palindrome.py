# Space Optimization Method: The above code can be space optimized by using only 1d array instead of 2d array. 
# In the dp table we only need previous row and current row elements.

# An LCS based program to find minimum number 
# insertions needed to make a string palindrome 

# Returns length of LCS for X[0..m-1], Y[0..n-1]. 
def lcs(X, Y, m, n): 
	prev = [0 for i in range(n+1)] 
	curr = [0 for i in range(n+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0: 
				prev[j] = 0
			elif X[i-1] == Y[j-1]: 
				curr[j] = prev[j-1]+1
			else: 
				curr[j] = max(prev[j], curr[j-1]) 
		prev = curr 

	# L[m][n] contains length of LCS for X[0..n-1] 
	# and Y[0..m-1] 
	return prev[n] 

def reverseStr(str): 
	return str[::-1] 

# LCS based function to find minimum number of 
# insertions 
def findMinInsertionsLCS(str, n): 

	# Create another string to store reverse of 'str' 
	rev = reverseStr(str) 

	# The output is length of string minus length of lcs of 
	# str and it reverse 
	return (n - lcs(str, rev, n, n)) 

# Driver code 
if __name__ == "__main__": 
	str = "geeks"
	print(findMinInsertionsLCS(str, len(str))) 

# Output
# 3
# Time complexity: O(N2) 
# Auxiliary Space: O(N)
