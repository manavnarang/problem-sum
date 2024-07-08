# We can build above four arrays in O(n) time by using Kadane Algorithm.

# In order to calculate maximum sum subarray that lies in arr[0…i], we run Kadane Algorithm from 0 to n-1 and to find maximum sum subarray that lies in arr[i+1 … n-1], we run Kadane Algorithm from n-1 to 0.
# Kadane’s algorithm can be modified to find minimum absolute sum of a subarray as well. The idea is to change the sign of each element in the array and run Kadane Algorithm to find maximum sum subarray that lies in arr[0…i] and arr[i+1 … n-1]. Now invert the sign of maximum subarray sum found. That will be our minimum subarray sum. This idea is taken from here.
# Now from above four arrays, we can easily find maximum absolute difference between the sum of two contiguous sub-arrays. For each index i, take maximum of

# abs(max sum subarray that lies in arr[0…i] – min sum subarray that lies in arr[i+1…n-1])
# abs(min sum subarray that lies in arr[0…i] – max sum subarray that lies in arr[i+1…n-1])
# Below is the implementation of above idea. 

# Python3 program to find two non-
# overlapping contiguous sub-arrays
# such that the absolute difference
# between the sum of two sub-array is maximum.

# Find maximum subarray sum for
# subarray [0..i] using standard
# Kadane's algorithm. This version 
# of Kadane's Algorithm will work if 
# all numbers are negative.
def maxLeftSubArraySum(a, size, sum):

	max_so_far = a[0]
	curr_max = a[0]
	sum[0] = max_so_far

	for i in range(1, size):
	
		curr_max = max(a[i], curr_max + a[i])
		max_so_far = max(max_so_far, curr_max)
		sum[i] = max_so_far
	
	return max_so_far

# Find maximum subarray sum for
# subarray [i..n] using Kadane's
# algorithm. This version of Kadane's
# Algorithm will work if all numbers are negative
def maxRightSubArraySum(a, n, sum):

	max_so_far = a[n]
	curr_max = a[n]
	sum[n] = max_so_far

	for i in range(n - 1, -1, -1):
	
		curr_max = max(a[i], curr_max + a[i])
		max_so_far = max(max_so_far, curr_max)
		sum[i] = max_so_far

	return max_so_far

# The function finds two non-overlapping
# contiguous sub-arrays such that the
# absolute difference between the sum
# of two sub-array is maximum.
def findMaxAbsDiff(arr, n):

	# create and build an array that 
	# stores maximum sums of subarrays 
	# that lie in arr[0...i]
	leftMax = [0 for i in range(n)]
	maxLeftSubArraySum(arr, n, leftMax)

	# create and build an array that stores
	# maximum sums of subarrays that lie in
	# arr[i+1...n-1]
	rightMax = [0 for i in range(n)]
	maxRightSubArraySum(arr, n-1, rightMax)

	# Invert array (change sign) to 
	# find minimum sum subarrays.
	invertArr = [0 for i in range(n)]
	for i in range(n):
		invertArr[i] = -arr[i]

	# create and build an array that stores
	# minimum sums of subarrays that lie in
	# arr[0...i]
	leftMin = [0 for i in range(n)]
	maxLeftSubArraySum(invertArr, n, leftMin)
	for i in range(n):
		leftMin[i] = -leftMin[i]

	# create and build an array that stores
	# minimum sums of subarrays that lie in
	# arr[i+1...n-1]
	rightMin = [0 for i in range(n)]
	maxRightSubArraySum(invertArr, n - 1, rightMin)
	for i in range(n):
		rightMin[i] = -rightMin[i]

	result = -2147483648
	for i in range(n - 1):
	
		''' For each index i, take maximum of
		1. abs(max sum subarray that lies in arr[0...i] -
			min sum subarray that lies in arr[i+1...n-1])
		2. abs(min sum subarray that lies in arr[0...i] -
			max sum subarray that lies in arr[i+1...n-1]) '''
		absValue = max(abs(leftMax[i] - rightMin[i + 1]),
					abs(leftMin[i] - rightMax[i + 1]))
		if (absValue > result):
			result = absValue
	
	return result
	
# Driver Code
a = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(a)
print(findMaxAbsDiff(a, n))

# Output
# 12
# Time Complexity is O(n) where n is the number of elements in input array. Auxiliary Space required is O(n). 
