'''
     Find all  triplets with zero sum using Hashing
     
     Below is the idea to solve the problem
    
    This involves traversing through the array. For every element arr[i], find a pair with sum “-arr[i]”. 
    This problem reduces to pair sum and can be solved in O(n) time using hashing.
    
    Follow the steps below to implement the idea:
    
    1. Create a HashSet to store a unique element.
    2. Run a nested loop with two loops, the outer loop from 0 to n-2 and the inner loop from i+1 to n-1
    3. Check if the sum of ith and jth element multiplied with -1 is present in the HashSet or not
    4. If the element is present in the HashSet, print the triplet else insert the jth element in the HashSet.
    Time Complexity: O(n2), Since two nested loops are required, so the time complexity is O(n2).
    Auxiliary Space: O(n), Since a HashSet is required, so the space complexity is linear.
'''

def findTriplets(arr, n):
    found = False
    for i in range(n - 1):

        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if found == False:
        print("No Triplet Found")


# Driver Code
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)

//OutPut
// -1 0 1
// -3 2 1

// Optimal Solution
// The time complexity here is O(N) and the space complexity is O(1).
// 1 2 -3
  
def find_triplet(arr):
    N = len(arr)
    for i in range(N - 2):
        if arr[i] + arr[i + 1] + arr[i + 2] == 0:
            print(arr[i], arr[i + 1], arr[i + 2])
            return
    print("No such triplet available")

if __name__ == "__main__":
    arr = [1, 2, -3, 4, -1, -2, 0]
    find_triplet(arr)
