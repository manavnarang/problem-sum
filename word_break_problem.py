# Word Break Problem | (Hashmap solution):
# In this approach first, we are storing all the words in a Hashmap. 
# after that, we traverse the input string and check if there is a match or not. 

def CanParseUtil(mp,word):

    # if the size id zero that means we completed the word. so we can return True
    size = len(word)
    if(size == 0):
        return True
    
    temp = ""
    for i in range(len(word)):
    
        temp += word[i]
        # if the temp exist in hashmap and the parsing operation of the remaining word is True, we can return True.
        if(temp in mp and CanParseUtil(mp, word[i+1:])):
        
            return True
        
    # if there is a mismatch in the dictionary, we can return false.
    return False

def CanParse(words,word):

    start = 0
    # store the words in the hashmap
    mp = {} 
    for it in words:
        mp[it] = True
    
    return "YES" if CanParseUtil(mp,word ) == True else "NO"


# driver code

words = ["mobile","samsung","sam","sung",
         "man","mango","icecream","and",
         "go","i","like","ice","cream"]
word = "samsungandmangok"
print(CanParse(words, word))

# Output
# NO
# Time Complexity: The time complexity of the above code will be O(2^n).
# Auxiliary Space: The space complexity will be O(n) as we are using recursion and the recursive call stack will take O(n) space.
