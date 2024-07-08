# (Nonnegative Numbers)

# # Using Sliding Window – O(N) time and O(1) auxiliary space
# The idea is simple, as we know that all the elements in subarray are positive so, 
# If a subarray has sum greater than the given sum then there is no possibility 
# that adding elements to the current subarray will be equal to the given sum. 
# So the Idea is to use a similar approach to a sliding window. 

# 1. Start with an empty subarray 
# 2. add elements to the subarray until the sum is less than k( given sum). 
# 3. If the sum is greater than k, remove elements from the start of the current subarray.

def subarray_sum(arr, n, sum):
    last = 0
    start = 0
    currsum = 0
    flag = False
    res = []

    # Iterate over the array
    for i in range(n):
        # Store sum up to current element
        currsum += arr[i]

        # Check if current sum is greater than or equal to given number
        if currsum >= sum:
            last = i

            # Start from starting index till current index
            while sum < currsum and start < last:
                # Subtract the element from left
                currsum -= arr[start]
                start += 1

            # If current sum becomes equal to given number
            if currsum == sum:
                res.append(start + 1)
                res.append(last + 1)
                flag = True
                break

    # If no subarray is found, store -1 in result
    if not flag:
        res.append(-1)

    # Return the result
    return res


# Driver Code
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23
res = subarray_sum(arr, n, sum)
for i in res:
    print(i, end=" ")

# Output
# 2 5 

# Time Complexity: O(N), where N is the length of input array
# Auxiliary Space: O(1). Since no extra space has been taken.
