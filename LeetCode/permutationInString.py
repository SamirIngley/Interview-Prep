''' Given two strings s1 and s2, write a function to return true is s2 contains
the permutation of s1. In other words, one of the first string's permutations
is the substring of the second string.

Note: Input strings only contain lower case letters. 
The length of both given strings is in range [1, 10,000]

Example 1:
Input: s1 = 'ab' s2='eidbaooo'
Output: True
s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1='ab' s2='eidboaoo'
Output: False 
'''

''' 
Brainstorm - so we need to get all the permutations of the first string
then loop through the second string and see if any match up. 

We can do this by going through each perm and creating a stack of that length 
then pushing and popping to the stack as we loop thorugh string.
If the first letter matches, the first of the substring, we check. 

Question: repeats allowed? Assume No
'''

def perms(s):
    l = []

    for item in s:
        if len(s) == 0: return []
        if len(s) == 1: return [s]

        for i in range(len(s)):
            
            place = s[i]

            remaining = s[:i] + s[i+1:]

            for newi in perms(remaining):
                l.append([place] + newi)
        
        return l

def itemInStr(item, yourstr):
    ''' item we're looking for, yourstring we look in'''

    # stack is the length of the item we're looking for,
    # we pull all the substrings from yourstring. 
    stack = [None]*len(item)
    found = False

    # looping through the big string and adding to the stack
    # which we need to pop and append (it's already the corect size for item we're looking for)
    for i in yourstr:

        # adding to the stack 
        stack.pop(0)
        stack.append(i)
    
        # if char at each index of stack and item match
        for num in range(len(stack)):
            if stack[num] == item[num]: 
                if num == len(stack)-1:
                    found = True
                    return found, stack
                else: continue
            else: break
    
    return 1



def permInStr(s1, s2):

    permlist = [p for p in perms(s1)]
    
    for perm in permlist:
        print(itemInStr(perm, s2))
    
    return 


newstring = [1,2,3,4,5,6]
checkme = [4,3]

[print(p) for p in perms(newstring)]

permInStr(checkme, newstring)