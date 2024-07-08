// Efficient Solution:

// If we drown a recursion tree of the above code, we can notice that the same values appear multiple times. 
// So we store results that are used later if repeated.

# Python 3 program to count number of strings
# of n characters with
 
# n is total number of characters.
# bCount and cCount are counts of 'b'
# and 'c' respectively.
// Output
// 19
def countStrUtil(dp, n, bCount=1,cCount=2):
 
    # Base cases
    if (bCount < 0 or cCount < 0):
        return 0
    if (n == 0):
        return 1
    if (bCount == 0 and cCount == 0):
        return 1
 
    # if we had saw this combination previously
    if (dp[n][bCount][cCount] != -1):
        return dp[n][bCount][cCount]
 
    # Three cases, we choose, a or b or c
    # In all three cases n decreases by 1.
    res = countStrUtil(dp, n-1, bCount, cCount)
    res += countStrUtil(dp, n-1, bCount-1, cCount)
    res += countStrUtil(dp, n-1, bCount, cCount-1)
 
    dp[n][bCount][cCount] = res
    return dp[n][bCount][cCount]
 
# A wrapper over countStrUtil()
def countStr(n):
 
    dp = [ [ [-1 for x in range(2+1)] for y in range(1+1)]for z in range(n+1)]
    return countStrUtil(dp, n)
 
# Driver code
if __name__ == "__main__":
     
    n = 3 # Total number of characters
    print(countStr(n))

# Time Complexity : O(n) 
# Auxiliary Space : O(n)


# # A solution that works in O(1) time :
# Let us proceed towards the solution step by step.

# How many strings we can form with no ‘b’ and ‘c’? 
# The answer is 1 because we can arrange a string consisting of only ‘a’ in one way only and the string would be aaaa….(n times).

# How many strings we can form with one ‘b’? 
# The answer is n because we can arrange a string consisting (n-1) ‘a’s and 1 ‘b’ is n!/(n-1)! = n . The same goes for ‘c’ .

# How many strings we can form with 2 places, filled up by ‘b’ and/or ‘c’ ?  
# Answer is n*(n-1) + n*(n-1)/2 . Because that 2 places can be either 1 ‘b’ and 1 ‘c’  or 2 ‘c’ according to our given constraints. 
# For the first case, total number of arrangements is n!/(n-2)! = n*(n-1) and for second case that is n!/(2!(n-2)!) = n*(n-1)/2 .

# Finally, how many strings we can form with 3 places, filled up by ‘b’ and/or ‘c’ ?  
# Answer is (n-2)*(n-1)*n/2 . Because those 3 places can only be consisting of 1 ‘b’ and 2’c’  according to our given constraints. 
# So, total number of arrangements is n!/(2!(n-3)!) = (n-2)*(n-1)*n/2 .

# A O(1) Python3 program to find 
# number of strings that can be
# made under given constraints.
 
def countStr(n):
    return (1 + (n * 2) +
                (n * ((n * n) - 1) // 2))
 
# Driver code 
if __name__ == "__main__":
    n = 3
    print(countStr(n))

# Output
# 19
# Time Complexity : O(1) 
# Auxiliary Space : O(1)
