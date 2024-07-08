# This problem reduces to finding if a string is subsequence of another string or not. 
# We traverse all dictionary words and for every word, we check if it is subsequence of given string and is largest of all such words. 
# We finally return the longest word with given string as subsequence.

# Below is the implementation of above idea  

# Python3 program to find largest word in Dictionary
# by deleting some characters of given string

# Returns true if str1[] is a subsequence of str2[].
# m is length of str1 and n is length of str2
def isSubSequence(str1, str2):

	m = len(str1);
	n = len(str2);

	j = 0; # For index of str1 (or subsequence

	# Traverse str2 and str1, and compare current
	# character of str2 with first unmatched char
	# of str1, if matched then move ahead in str1
	i = 0;
	while (i < n and j < m):
		if (str1[j] == str2[i]):
			j += 1;
		i += 1;

	# If all characters of str1 were found in str2
	return (j == m);

# Returns the longest string in dictionary which is a
# subsequence of str.
def findLongestString(dict1, str1):
	result = "";
	length = 0;

	# Traverse through all words of dictionary
	for word in dict1:
		
		# If current word is subsequence of str and is largest
		# such word so far.
		if (length < len(word) and isSubSequence(word, str1)):
			result = word;
			length = len(word);

	# Return longest string
	return result;

# Driver program to test above function

dict1 = ["ale", "apple", "monkey", "plea"];
str1 = "abpcplea" ;
print(findLongestString(dict1, str1));

# Output
# apple

# Time Complexity: O(N*(K+n)) Here N is the length of dictionary and n is the length of given string ‘str’ and K – maximum length of words in the dictionary.
# Auxiliary Space: O(1)  


# An efficient solution is we Sort the dictionary word. 
# We traverse all dictionary words and for every word, we check if it is subsequence of given string and at last we check this subsequence  is largest of all such subsequence. 
# We finally return the longest word with given string as subsequence.

# Python3 program to find largest word in Dictionary
# by deleting some characters of given string

res=""

def check(d,s):
	global res
	i = 0
	j = 0
	while(i < len(d) and j < len(s)):

		if(d[i] == s[j]):
			i += 1
			j += 1
		else:
			j += 1

		if(i == len(d) and len(res) < len(d)):
			res = d

def LongestWord(d, S):

	# sort the dictionary word
	# for smallest lexicographical order 
	d.sort()

	for c in d :
		check(c,S)
	
	return res

# Driver program 
dict = [ "ale", "apple", "monkey", "plea" ]
str = "abpcplea"
print(LongestWord(dict, str))
# Output
# apple

