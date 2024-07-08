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
