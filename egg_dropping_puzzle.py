# Egg Dropping Puzzle using space-optimized DP:
# The fourth approach can be optimized to 1-D DP as for calculating the current row of the DP table, 
# we require only the previous row results and not beyond that.

# Follow the below steps to solve the problem:

# 1. Create an array dp of size N+1 and an integer m
# 2. Run a for loop from m equal to zero till dp[n] < k
# 3. Run a nested for loop from x equal to n till x is greater than zero
# 4. Set dp[x] equal to 1 + dp[x-1]
# 5. Return m
# Below is the implementation of the above approach:

# Python implementation for the above approach.


def minTrials(n, k):
    # Initialize array of size (n+1) and m as moves.
    dp = [0 for i in range(n+1)]
    m = 0
    while dp[n] < k:
        m += 1
        for x in range(n, 0, -1):
            dp[x] += 1 + dp[x - 1]
    return m


# Driver code
n, k = 2, 36
print("Minimum number of trials in worst case with",
      n, "eggs and", k, "floors is", minTrials(n, k))

# This code is contributed by Amit Mangal.

# Output
# Minimum number of trials in worst case with 2 eggs and 36 floors is 8
# Time Complexity: O(N * K)
# Auxiliary Space: O(N)
