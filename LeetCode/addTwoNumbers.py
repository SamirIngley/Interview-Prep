# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Restate: We are given two numbers whose individual digits are trapped in reverse order in a linked list. 
# Return the sum of those numbers as a linked list not in reverse order. 

# Questions: 
# Assumptions: 

# Thought Process:
# After solving a sample problem on paper it becomes clear: do not add each number individually by traversing both lists at once bc
# carrying over the numbers is difficult
# Do traverse the list and prepend each item to an array, join the array into a string, convert the string into an integer. 
# Do the same for the next linked list and sum the two numbers. 

# Start a new linked list and add a digit from the sum into each node until no more numbers remain.
# -----------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
         
