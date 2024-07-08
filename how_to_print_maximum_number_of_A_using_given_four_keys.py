# Below is Dynamic Programming based python implementation where an auxiliary array screen[N] is used to store result of subproblems. 
# As the number of A’s become large, the effect of pressing Ctrl-V more than 3 times starts 
# to become insubstantial as compared to just pressing Ctrl-A, Ctrl-C and Ctrl-V again.

# A Dynamic Programming based Python3 program 
# to find maximum number of A's
# that can be printed using four keys 

# this function returns the optimal 
# length string for N keystrokes
def findoptimal(N):

	# The optimal string length is 
	# N when N is smaller than 7
	if (N <= 6):
		return N

	# An array to store result of 
	# subproblems
	screen = [0] * N

	# Initializing the optimal lengths 
	# array for until 6 input
	# strokes.
	
	for n in range(1, 7):
		screen[n - 1] = n

	# Solve all subproblems in bottom manner
	for n in range(7, N + 1):
		
		# for any keystroke n, we will need to choose between:-
		# 1. pressing Ctrl-V once after copying the
		# A's obtained by n-3 keystrokes.

		# 2. pressing Ctrl-V twice after copying the A's
		# obtained by n-4 keystrokes.

		# 3. pressing Ctrl-V thrice after copying the A's
		# obtained by n-5 keystrokes.
		screen[n - 1] = max(2 * screen[n - 4], 
						max(3 * screen[n - 5], 
							4 * screen[n - 6]));
		
	return screen[N - 1]

# Driver Code
if __name__ == "__main__":

	# for the rest of the array we 
	# will reply on the previous
	# entries to compute new ones
	for N in range(1, 21):
		print("Maximum Number of A's with ", N,
			" keystrokes is ", findoptimal(N))

# Output: 

# Maximum Number of A's with 1 keystrokes is 1
# Maximum Number of A's with 2 keystrokes is 2
# Maximum Number of A's with 3 keystrokes is 3
# Maximum Number of A's with 4 keystrokes is 4
# Maximum Number of A's with 5 keystrokes is 5
# Maximum Number of A's with 6 keystrokes is 6
# Maximum Number of A's with 7 keystrokes is 9
# Maximum Number of A's with 8 keystrokes is 12
# Maximum Number of A's with 9 keystrokes is 16
# Maximum Number of A's with 10 keystrokes is 20
# Maximum Number of A's with 11 keystrokes is 27
# Maximum Number of A's with 12 keystrokes is 36
# Maximum Number of A's with 13 keystrokes is 48
# Maximum Number of A's with 14 keystrokes is 64
# Maximum Number of A's with 15 keystrokes is 81
# Maximum Number of A's with 16 keystrokes is 108
# Maximum Number of A's with 17 keystrokes is 144
# Maximum Number of A's with 18 keystrokes is 192
# Maximum Number of A's with 19 keystrokes is 256
# Maximum Number of A's with 20 keystrokes is 324
# Time Complexity: O(N)
# Auxiliary Space: O(N)
