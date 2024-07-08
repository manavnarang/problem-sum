# 4Sum solution having no duplicate elements:
# Store sums of all pairs in a hash table
# Traverse through all pairs again and search for X – (current pair sum) in the hash table.
# Consider a temp array that is initially stored with zeroes. It is changed to 1 when we get 4 elements that sum up to the required value.
# If a pair is found with the required sum, then make sure that all elements are distinct array elements and check if the value in temp array is 0 so that duplicates are not considered.
# Below is the implementation of the code: 
# Without using extra spaces:

def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            k, l = j + 1, n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1
    
    return result

# Example usage
nums = [10, 2, 3, 4, 5, 9, 7, 8]
target = 23
print(four_sum(nums, target))

# Output :
# 1 20 30 40

# Complexity Analysis:
# Time complexity: O(n^2).
# Auxiliary Space: O(1)
