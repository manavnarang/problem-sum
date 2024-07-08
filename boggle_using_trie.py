# OPTIMIZED APPROACH WITHOUT USING TRIE ( Short and Easy to understand with a better Time and Space complexity):

# First, we create a Set Data Structure and add all word in it to avoid duplicate word.
# Then we make a new array of type String and add those set elements to it.
# We check word by word using a for loop whether that particular word is present in the board and if it returns true , we shall add it our ArrayList<String>.
# While searching for a word in the board,we shall use backtracking so that while coming back,we can alter the board as it was before.
# Lastly we sort the array and print it.

# Python code addition 

def exist(board, word, r, c):
	for i in range(r):
		for j in range(c):
			if board[i][j] == word[0] and search(board, word, 0, i, j, r, c):
				return True
	return False

def search(board, word, length, i, j, r, c):
	if i < 0 or i >= r or j < 0 or j >= c:
		return False

	if board[i][j] != word[length]:
		return False

	if length == len(word) - 1:
		return True

	ch = board[i][j]
	board[i][j] = '@'

	ans = search(board, word, length+1, i-1, j, r, c) or \
		search(board, word, length+1, i+1, j, r, c) or \
		search(board, word, length+1, i, j-1, r, c) or \
		search(board, word, length+1, i, j+1, r, c) or \
		search(board, word, length+1, i-1, j+1, r, c) or \
		search(board, word, length+1, i-1, j-1, r, c) or \
		search(board, word, length+1, i+1, j-1, r, c) or \
		search(board, word, length+1, i+1, j+1, r, c)

	board[i][j] = ch
	return ans

def word_boggle(board, dictionary):
	r, c = 3, 3

	temp = []
	st = set(dictionary)
	n = len(st)

	dict = []
	for s in st:
		dict.append(s)

	for i in range(n):
		if exist(board, dict[i], r, c):
			temp.append(dict[i])

	return temp


if __name__ == '__main__':
	dictionary = ["GEEKS", "FOR", "QUIZ", "GEE"]

	boggle = [['G', 'I', 'Z'],
			['U', 'E', 'K'],
			['Q', 'S', 'E']]

	ans = word_boggle(boggle, dictionary)

	if len(ans) == 0:
		print("-1")
	else:
		ans.sort()
		print(" ".join(ans))

# Output
# GEE GEEKS QUIZ 
# Time Complexity: O(N*W + R*C^2)
# Space Complexity: O(N*W + R*C)
