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

newstring = [1,2,3,4,5,6]

for p in perms(newstring):
    print(p)