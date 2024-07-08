# Method 1 (Brute Force) 
# If the length of string is n, then there can be n*(n+1)/2 possible substrings. 
# A simple way is to generate all the substring and check each one whether it has exactly k unique characters or not. 
# If we apply this brute force, it would take O(n2) to generate all substrings and O(n) to do a check on each one. 
# Thus overall it would go O(n3).

# We can further improve this solution by creating a hash table and while generating the substrings, 
# check the number of unique characters using that hash table. Thus it would improve up to O(n2).

# Python program to find the longest substring
# with k unique characters in a given string

# Function to calculate length of
# longest substring with k characters
def longestKSubstr(s, k):
	n = len(s)
	answer = -1
	for i in range(n):
		for j in range(i+1, n+1):
			distinct = set(s[i:j])
			if len(distinct) == k:
				answer = max(answer, j - i)
	print(answer)

s = "aabacbebebe"
k = 3

# Function Call
longestKSubstr(s, k)

# Output
# 7
# Time Complexity: O(n^2) 
# Auxiliary Space: O(n)

# # Other Methods:
# Method 2 (Linear Time) 
# ANOTHER APPROACH:(Linear Time)
