# Dynamic Programming: Its an unbounded knapsack problem as we can use 1 or more instances of any resource. 
# A simple 1D array, say dp[W+1] can be used such that dp[i] stores the maximum value which can achieved 
# using all items and i capacity of knapsack. 
# Note that we use 1D array here which is different from classical knapsack where we used 2D array. 
# Here number of items never changes. We always have all items available.
# We can recursively compute dp[] using below formula

# dp[i] = 0
# dp[i] = max(dp[i], dp[i-wt[j]] + val[j] 
#                    where j varies from 0 
#                    to n-1 such that:
#                    wt[j] <= i
# result = d[W]
# Below is the implementation of above idea. 

 
# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.

# Returns the maximum value 
# with knapsack of W capacity
def unboundedKnapsack(W, n, val, wt):

    # dp[i] is going to store maximum 
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]

    ans = 0

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[W]

# Driver program
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)

print(unboundedKnapsack(W, n, val, wt))

# Output
# 300
# Time Complexity: O(W*N) where W is the total weight(capacity) and N is the total number of items.
# Auxiliary Space: O(W) where W is the total weight.
