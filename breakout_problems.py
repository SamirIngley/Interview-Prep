from math import ceil

# Given a list of n numbers, determine if it contains any duplicate numbers.
# Jessica Trinh

# Find duplicates in an array of numbers 

# Numbers are whole 
# Account for negatives
# Assume that the list of numbers is unsorted 
# Return Bool for whether or not a duplicate exists 
# And number that appears 2+ is a duplicate 

# Example: 

# [-3, 5, 6, -7, 8, 9, 10, 11, 5, 10, 2, -6] → True 

# Walkthrough: 

# Option A: 
# Sort the array
# As we’re looping through, if the value already exists in the set, return True 

# Option B: 
# Loop through the indexes and append each value to a set if the value doesn’t already exist in the set 
# Compare the sorted list to the set 
# Equal in length first 
# See if the values of list are equal
# If they are, then return true 
# If not then False 

# Option C:
# Samir Ingle
# we only need to find the first set of duplicates we can find
# sort the list, check if the current item is the same as the preivous item


def checkDuplicates(new_list): 
    new_list.sort() 
    # print(new_list)
    previous = None
    for item in new_list:
        # print(previous, item)
        if previous == item:
            return True
        previous = item
    return False


# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes. 
# Samir Ingle

# Restate: Middle item(s) in a singly linked list. 
# Questions: none
# Assumptions: Since it’s a linked list… no indexes

# Example:
# A > B > C > D > E > F > G

# middle = length of the list/ 2
# if the middle is a fraction:
# 	middle1 = ceiling(middle)
# 	middle2 = floor(middle)
# 	return middle1, middle2
# else:
# 	return middle
# Code:

def findMiddle(ll):
    current = ll.head			# start at the head of the linked list
    ll_length = 0
    odd = False

    while current:				# while a node exists in the ll
        ll_length += 1			# add 1 to the length counter
        current = current.next		# move on to the next node 

    if ll_length % 2 != 0:			# if the LL is odd
        middle = ceil(ll_length/2)
        odd = True
        return middle
    else:
        middle = ll_length/2

    index = 0
    while index != middle:
        current = current.next
    if odd == True:
        return current, current.next
    return current


# Find the longest substring of unique letters in a given string of n letters.


# Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.

if __name__ == "__main__":
    checkDuplicates([1,2,3,4,5,2])
