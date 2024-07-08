//Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, 
// generate all binary strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’. 

// Method 1 (Using Recursion) 
// Method 2 (Using Queue) 
// Method 3 (Using str and Recursion) -- using

#we store processed strings in all (array)
#we see if string as "?", if so, replace it with 0 and 1
#and send it back to recursive func until base case is reached
#which is no wildcard left
 
res = []
def genBin(s):
    if '?' in s:
        s1 = s.replace('?','0',1) #only replace once
        s2 = s.replace('?','1',1) #only replace once
        genBin(s1)
        genBin(s2)
    else: res.append(s)
 
# Driver code
genBin("1??0?101")
print(res)

Output: 
['10000101', '10001101', '10100101', '10101101', '11000101', '11001101', '11100101', '11101101']

Time Complexity: O(N*2N),  where N is the size of the string.
Auxiliary Space: O(2N)


// Method 1 (Using Recursion) 
'''
    We pass index of next character to the recursive function. 
    If the current character is a wildcard character ‘?’, 
    we replace it with ‘0’ or ‘1’ and do the same for all remaining characters. 
    We print the string if we reach at its end. 

Algorithm:
Step 1: Initialize the string first with some wildcard characters in it.
Step 2: Check if index position is equals to the size of string, If it is return.
Step 3: If wildcard character is present at index location, replace it by 0 or 1 accordingly.
Step 4: Print the output
Time Complexity: O(2N), where N is the length of the given string and there are 2 possibilities.
Auxiliary Space: O(N2), as a copy of the string is created in every recursive call.

Below is the implementation of the above approach:
'''
# Recursive Python program to generate all
# binary strings formed by replacing
# each wildcard character by 0 or 1
 
# Recursive function to generate all binary
# strings formed by replacing each wildcard
# character by 0 or 1
def _print(string, index):
    if index == len(string):
        print(''.join(string))
        return
 
    if string[index] == "?":
 
        # replace '?' by '0' and recurse
        string[index] = '0'
        _print(string, index + 1)
 
        # replace '?' by '1' and recurse
        string[index] = '1'
        _print(string, index + 1)
 
        # NOTE: Need to backtrack as string
        # is passed by reference to the
        # function
        string[index] = '?'
    else:
        _print(string, index + 1)
 
# Driver code
if __name__ == "__main__":
 
    string = "1??0?101"
    string = list(string)
    _print(string, 0)
# Output: 
# 10000101
# 10001101
# 10100101
# 10101101
# 11000101
# 11001101
# 11100101
# 11101101
 
# Note: function name _print is used because
# print is already a predefined function in Python
