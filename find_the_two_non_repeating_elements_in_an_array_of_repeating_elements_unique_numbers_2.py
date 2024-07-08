# Non Repeating Numbers using Sorting:
# Time complexity: O(n log n)
# Auxiliary Space: O(1)
# Non Repeating Numbers using XOR:--- using
# Time Complexity: O(n) 
# Auxiliary Space: O(1)

# Function to find two non-repeating numbers in an array
def get_2_non_repeating_nos(nums):
    # Pass 1:
    # Get the XOR of the two numbers we need to find
    diff = 0
    for num in nums:
        diff ^= num

    # Get its last set bit
    diff &= -diff

    # Pass 2:
    rets = [0, 0]  # this list stores the two numbers we will return
    for num in nums:
        if (num & diff) == 0:  # the bit is not set
            rets[0] ^= num
        else:  # the bit is set
            rets[1] ^= num

    # Ensure the order of the returned numbers is consistent
    if rets[0] > rets[1]:
        rets[0], rets[1] = rets[1], rets[0]

    return rets

# Driver code
arr = [2, 3, 7, 9, 11, 2, 3, 11]
result = get_2_non_repeating_nos(arr)
print("The non-repeating elements are", result[0], "and", result[1])

# Output
# The non-repeating elements are 7 and 9

# First, calculate the XOR of all the array elements. xor = arr[0]^arr[1]^arr[2]…..arr[n-1]

# All the bits that are set in xor will be set in one non-repeating element (x or y) and not in others. 
# So if we take any set bit of xor and divide the elements of the array in two sets – one set of elements with same bit set and another set with same bit not set. 
# By doing so, we will get x in one set and y in another set. Now if we do XOR of all the elements in the first set, we will get the first non-repeating element, 
# and by doing same in other sets we will get the second non-repeating element.

# Illustration:

# We have the array: [2, 4, 7, 9, 2, 4]

# XOR = 2 ^ 4 ^ 7 ^ 9 ^ 2 ^ 4 = 2 ^ 2 ^ 4 ^ 4 ^ 7 ^ 9 = 0 ^ 0 ^ 7 ^ 9 = 7 ^ 9 = 14
# The rightmost set bit in binary representation of 14 is at position 1 (from the right).
# Divide the elements into two groups based on the rightmost set bit.
# Group 1 (rightmost bit set at position 1): [2, 7, 2]
# Group 2 (rightmost bit not set at position 1): [4, 9, 4]
# XOR all elements in Group 1 to find one non-repeating element.
# Non-repeating element 1 = 2 ^ 7 ^ 2 = 7
# XOR all elements in Group 2 to find the other non-repeating element.
# Non-repeating element 2 = 4 ^ 9 ^ 4 = 9
# The two non-repeating elements are 7 and 9,
