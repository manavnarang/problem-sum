# # A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1. 
# An Efficient Solution can solve this problem in O(k) time where k is number of Jumping Numbers smaller than or equal to x. The idea is use BFS or DFS. 
# Assume that we have a graph where the starting node is 0 and we need to traverse it from the start node to all the reachable nodes.
# With the restrictions given in the graph about the jumping numbers, what do you think should be the restrictions defining the next transitions in the graph.
# Lets take a example for input x = 90

# Start node = 0
# From 0, we can move to 1 2 3 4 5 6 7 8 9 
# [these are not in our range so we don't add it]

# Now from 1, we can move to 12 and 10 
# From 2, 23 and 21
# From 3, 34 and 32
# .
# .
# .
# .
# .
# .
# and so on.
# Class queue for use later
# Below is BFS based implementation of above idea. 
class Queue:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def enqueue(self, elem):
        self.lst.append(elem)

    def dequeue(self):
        return self.lst.pop(0)

# Prints all jumping numbers smaller than or equal to
# x starting with 'num'. It mainly does BFS starting
# from 'num'.
def bfs(x, num):

    # Create a queue and enqueue i to it
    q = Queue()
    q.enqueue(num)

    # Do BFS starting from 1
    while (not q.is_empty()):
        num = q.dequeue()

        if num<= x:
            print(str(num), end =' ')
            last_dig = num % 10

            # If last digit is 0, append next digit only
            if last_dig == 0:
                q.enqueue((num * 10) + (last_dig + 1))

            # If last digit is 9, append previous digit
            # only
            elif last_dig == 9:
                q.enqueue((num * 10) + (last_dig - 1))

            # If last digit is neither 0 nor 9, append
            # both previous digit and next digit
            else:
                q.enqueue((num * 10) + (last_dig - 1))
                q.enqueue((num * 10) + (last_dig + 1))

# Prints all jumping numbers smaller than or equal to
# a positive number x
def printJumping(x):
    print (str(0), end =' ')
    for i in range(1, 10):
        bfs(x, i)

# Driver Program ( Change value of x as desired )
x = 40
printJumping(x)
# Output
# 0 1 10 12 2 21 23 3 32 34 4 5 6 7 8 9 
# Time Complexity: O(k) time where k is number of Jumping Numbers smaller than or equal to x
# Auxiliary Space: O(1)
