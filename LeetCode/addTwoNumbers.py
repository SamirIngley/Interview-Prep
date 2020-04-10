# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Restate: We are given two numbers whose individual digits are trapped in reverse order in a linked list. 
# Return the sum of those numbers as a linked list not in reverse order. 

# Questions: Do you want the new linked list in reverse order? 
# Assumptions: According to the example it is in reverse order so I assume so. 

# Thought Process:
# After solving a sample problem on paper it becomes clear: do not add each number individually by traversing both lists at once bc
# carrying over the numbers is difficult
# Do traverse the list and prepend each item to an array, join the array into a string, convert the string into an integer. 
# Do the same for the next linked list and sum the two numbers. 

# Start a new linked list and add a digit from the sum into each node until no more numbers remain.
# -----------------------------------------
# ACCEPTED ANSWER:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
         num_array1 = []
         while l1:
            # print(l1.val)
            num_array1.insert(0, str(l1.val))
            l1 = l1.next
         # print(num_array1)
         n = ''
         num1 = n.join(num_array1)
         # print(int(num1))
            
         num_array2 = []
         while l2:
            # print(l2.val)
            num_array2.insert(0, str(l2.val))
            l2 = l2.next
         # print(num_array2)
       
         num2 = n.join(num_array2)
         # print(int(num2))
            
         sum_num = int(num1) + int(num2)
        
         result = ListNode(0)
         result_tail = result
            
         for item in str(sum_num)[::-1]:
            # print(item)
            result_tail.next = ListNode(item)
            result_tail = result_tail.next
        
         return result.next
            