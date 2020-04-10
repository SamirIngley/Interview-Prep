# Given an array a of numbers and a target value t, find two numbers that sum to t (that is, a[i] + a[j] = t).

# array of a numbers (int)
# target value t
# find two numbers that sum to target

# Restate:
# Find two numbers in the array that add up to the target value if they exist. 

# Clarifying questions
# Integers
# What if there are multiple that add to the target? Find the first one you can find

# T, loop the array we'll know the current value. 
# Subtract the two and see if the complement exists in the array. 
# Sort the array. 
# then go from either end move in until match is found. 

def Two_num(some_array, target):
    for item in some_array:
         if (target-item) in some_array:
             return print(item, target-item)
    return print('dne')

Two_num([-1,-2,-3,4,5,6,7,8,9], 7)


# 2. Given 2 arrays of `n` numbers each, find a pair of numbers (one from each array) whose sum is closest to a given target value `t`.

# O(n^2)


# 3. Reverse a linked list by reusing the nodes (do not create new nodes).

# Restate the problem:
# Flip around all the nodes in a linked list. 
# Reverse the order of nodes in the linked list. Without new nodes.

# Finally, switch the tail and head pointers

# Current node points to next node. 
# We want it to point to previous node. 

# We have a linked list
# iterate through each node. 
# store each node's previous node as the current node's next node. 
# If there is no previous node... then Call it the tail.
# if there is no next node.. call it the head. 
# A > B > C > D

def flip_list():
    current = self.head
    previous = None

    while current:
        if not previous:
            self.tail = current 
            previous = current
            current = current.next
            break
        else:
            next_pointer = current.next
            current.next = previous

# Find the k largest numbers in a an array of n numbers. Return them in an array sorted in decreasing order.



