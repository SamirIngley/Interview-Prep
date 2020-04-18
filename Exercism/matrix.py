# Exercism.io

# Given a string representing a matrix of numbers, return the rows and columns 
# of that matrix. 

# 1. Generate reasonable test inputs
# 2. Understand & solve the problem
# 3. Simplify the problem if needed
# 4. Find a pattern in your solution
# 5. Make a plan - write pseudocode
# 6. Follow your plan - write real code
# 7. Check your work - test your code


# INPUT: string of numbers with embedded newlines 
# 9 8 7
# 5 3 2
# 6 6 7

# OUTPUT: Number the rows and columns. 
#  1  2  3
#   |---------
# 1 | 9  8  7
# 2 | 5  3  2
# 3 | 6  6  7

# TESTS: 
# 1. Normal input: small example of how it's expected to run
# 2. Valid data types
# 3. Boundaries
# 4. Obeys assumptions on values



# STEPS: 

# 1. Reasonable test input:
# input string:
# print('9 8 7\n5 3 2\n6 6 7')

#output:

# 2. Understand and solve the problem: 
# For rows, identify the len of the row by finding the length from the first index to the 
# first new line. These are your rows, create a new row with these numbers at the right index. 
# For columns, identify and add a new column number after each newline

# 3. Simplify the problem:
# try only 1 number matrix 
# try only adding the rows, only adding columns

# input = ('3')

# 4. Find a pattern
# counter
# looking for \n

# 5. Write pseudocode:
# rows:
# set a counter for the number of characters before \n
# check if char "\" exists in string 
# while char != '\' 
# return 
# create a string with the numbers at every other place in the range of counter
# prepend this string to the matrix string

# columns:
# if first char, add 1 before string
# else add 1 to counter
# insert counter after \n

# 6. Write code:
# (below)

# 7. Check work: 



print('input matrix:\n9 8 7\n5 3 2\n6 6 7')
print('------------------')
input = '9 8 7\n5 3 2\n6 6 7'
# class add_RC(m8x_string):

    # def init(self, m8x_string):
        

def add_rows(m8x_string):
    row_count = 0
    row_string = ''
    for char in m8x_string:
        if char == ' ':
            continue
        if char == '\n':
            break 
        row_count += 1
        # print('char:', char, 'row_count', row_count)

    # print('final row count: ', row_count)
    for i in range(1, row_count+1):
        # print(i)
        row_string += '{} '.format(str(i))

    # print("row string ", row_string)
    m8x_string = row_string + "\n" + m8x_string
    print(m8x_string)
    return m8x_string

    # def add_columns(self):


if __name__ == "__main__":
    add_rows(input)