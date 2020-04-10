
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

def checkDuplicates(list): 
	sortedList = list.sort() 
	setList = set() 
	for item in sortedList: 
		setList.append(item): 
			if item in setList:
				return True
			else: 
				return False 


# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes. 
# Samir Ingle

# Restate: Middle item(s) in a singly linked list. 
# Questions: none
# Assumptions: Since it’s a linked list… no indexes

# Example:
# A > B > C > D > E > F > G

middle = length of the list/ 2
if the middle is a fraction:
	middle1 = ceiling(middle)
	middle2 = floor(middle)
	return middle1, middle2
else:
	return middle
Code:
def findMiddle():
	current = self.head			# start at the head of the linked list
	ll_length = 0
	odd = False
	while current:				# while a node exists in the ll
		ll_length += 1			# add 1 to the length counter
		current = current.next		# move on to the next node 
	if ll_length % 2 != 0:			# if the LL is odd
		middle = ceiling(ll_length/2)
		odd = True
		return middle
	else:
		middle = ll_length/2
return 

index = 0
while index != middle:
	current = current.next
if odd = True:
	return current, current.next
else:
return current


# Find the longest substring of unique letters in a given string of n letters.


# Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.
