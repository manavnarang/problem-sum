# Method 3: Dynamic Programming(Memoization)

# Approach: We can make a matrix where rows and columns represent the characters of the string A and B. 
# If C is the interleaved string of A and B then there exists a path from the top left of the Matrix to the bottom right. 
# That is if we can go from index 0,0 to n,m while matching characters of all A and B with C then C is interleaved of A and B.
# Let A be “XXY”, B be “XXZ” and C be “XXZXXY” then the path would look something like this:

#  	X	X	Y	 
# X	1	0	0	0
# X	1	0	0	0
# Z	1	0	0	0
#  	1	1	1	R
# let us consider one more example, let A be “ABC”, B be “DEF” and C be “ADBECF”, then the path would look something like this:

#  	D	E	F	 
# A	1	0	0	0
# B	1	1	0	0
# C	0	1	1	0
#  	0	0	1	R
# If there exists a path through which we can reach R, then C is the interleaved strings of A and B.
# Algorithm:
# 1. We will first create a matrix dp to store the path since one path can be explored multiple times, the Matrix index dp[i][j] will store if there exists a path from this index or not.
# 2. If we are at i’th index of A and j’th index of B and C[i+j] matches both A[i] and B[j] then we explore both the paths that are we will go right and down i.e. we will explore index i+1,j and j+1,i.
# 3. If C[i+j] only matches with A[i] or B[j] then we will go just down or right respectively that is i+1,j or i,j+1.

# A Python Memoization program
# to check whether a string C is
# an interleaving of two other
# strings A and B.

# Declare dp array
dp = [[0]*101]*101

# This function checks if there exist a valid path from 0,0 to n,m
def dfs(i, j, A, B, C):

    # If path has already been calculated from this index
    # then return calculated value.
    if(dp[i][j]!=-1):
        return dp[i][j]
        
    # If we reach the destination return 1
    n,m=len(A),len(B)
    if(i==n and j==m):
        return 1
    
    # If C[i+j] matches with both A[i] and B[j]
    # we explore both the paths
    
    if (i<n and A[i]==C[i + j] and j<m and B[j]==C[i + j]):
        # go down and store the calculated value in x
        # and go right and store the calculated value in y.
        x = dfs(i + 1, j, A, B, C)
        y = dfs(i, j + 1, A, B, C)
        
        # return the best of both.
        dp[i][j] = x|y
        return dp[i][j]
    
    # If C[i+j] matches with A[i].
    if (i < n and A[i] == C[i + j]):
        # go down
        x = dfs(i + 1, j, A, B, C)
        
        # Return the calculated value.
        dp[i][j] = x
        return dp[i][j]
    
    # If C[i+j] matches with B[j].
    if (j < m and B[j] == C[i + j]):
        y = dfs(i, j + 1, A, B, C)
        
        # Return the calculated value.
        dp[i][j] = y
        return dp[i][j]
    
    # if nothing matches we return 0
    dp[i][j] = 0
    return dp[i][j]

# The main function that 
# returns true if C is
# an interleaving of A 
# and B, otherwise false.
def isInterleaved(A, B, C):

    # Storing the length in n,m
    n = len(A)
    m = len(B)
    
    # C can be an interleaving of
    # A and B only of the sum
    # of lengths of A & B is equal
    # to the length of C.
    
    if((n+m)!=len(C)):
        return 0
    
    # initializing dp array with -1
    for i in range(n+1):
        for j in range(m+1):
            dp[i][j]=-1
    
    # calling and returning the answer
    return dfs(0,0,A,B,C)
    

# A function to run test cases
def test(A, B, C):

    if (isInterleaved(A, B, C)):
        print(C, "is interleaved of", A, "and", B)
    else:
        print(C, "is not interleaved of", A, "and", B)

# Driver Code
if __name__ == '__main__':
    test("XXY", "XXZ", "XXZXXXY")
    test("XY", "WZ", "WZXY")
    test("XY", "X", "XXY")
    test("YX", "X", "XXY")
    test("XXY", "XXZ", "XXXXZY")
    test("ACA", "DAS", "DAACSA")

# Output
# XXZXXXY is not interleaved of XXY and XXZ
# WZXY is interleaved of XY and WZ
# XXY is interleaved of XY and X
# XXY is not interleaved of YX and X
# XXXXZY is interleaved of XXY and XXZ
# DAACSA is interleaved of ACA and DAS

# Complexity Analysis:

# Time Complexity:  O(m*n).

# This is the worst case of time complexity, if the given strings contain no common character matching with C then the time complexity will be O(n+m).
# Space Complexity: O(m*n).

# This is the space required to store the DP array.
