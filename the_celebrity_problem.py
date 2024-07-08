# The Celebrity Problem using Two-pointer approach:
# The idea is to use two pointers, one from start and one from the end. 
# Assume the start person is A, and the end person is B. 
# If A knows B, then A must not be the celebrity. 
# Else, B must not be the celebrity. 
# At the end of the loop, only one index will be left as a celebrity. 
# Go through each person again and check whether this is the celebrity. 
# The Two Pointer approach can be used where two pointers can be assigned, 
# one at the start and the other at the end, 
# and the elements can be compared and the search space can be reduced. 

# Follow the steps below to solve the problem:
# 1. Create two indices i and j, where i = 0 and j = n-1
# 2. Run a loop until i is less than j.
# 3. Check if i knows j, then i can’t be a celebrity. so increment i, i.e. i++
# 4. Else j cannot be a celebrity, so decrement j, i.e. j–
# 5. Assign i as the celebrity candidate
# 6. Now at last check whether the candidate is actually a celebrity by re-running a loop from 0 to n-1  
# and constantly checking if the candidate knows a person or if there is a candidate who does not know the candidate.
# 7. Then we should return -1. else at the end of the loop, we can be sure that the candidate is actually a celebrity.
# Below is the implementation of the above approach:

# Python3 code
class Solution:

    # Function to find if there is a celebrity in the party or not.
    # return index if celebrity else return -1
    def celebrity(self, M, n):
        # code here
        i = 0
        j = n-1
        candidate = -1
        while(i < j):
            if M[j][i] == 1:
                j -= 1
            else:
                i += 1

        candidate = i
        for k in range(n):
            if candidate != k:
                if M[candidate][k] == 1 or M[k][candidate] == 0:
                    return -1

        return candidate


n = 4
m = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]
ob = Solution()
a = ob.celebrity(m, n)
if a == -1:
    print("No Celebrity")
else:
    print("Celebrity ID", a)

# Output
# Celebrity ID 2
# Time Complexity: O(N), Iterating two times the array of size N.
# Auxiliary Space: O(1) No extra space is required.
