# Imagine you are writing a function for a new code editor that will check
# if a string expression contains correctly balanced parentheses.
# this func will 


for item in string:
    if item == '(':
        left += 1
    elif item == ')':
        right += 1
if right != left:
    raise ERROR


USE A STACK add the opening brackets
if closing, check if it complements the first one on the stack !!

