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

# 3. Simplify the problem:
# try only 1 number matrix 
# try only adding the rows, only adding columns

# input = ('3')

# 4. Find a pattern
# counter
# looking for \n

# 5. Write pseudocode:
# rows:
# split at the newline
# iterate through each item in each new line

# columns:
# zip item in each row 


# 6. Write code:
# (below)

# 7. Check work: 



print('input matrix:\n9 8 7\n5 3 2\n6 6 7')
print('------------------')

class Matrix_Rows_Columns():
    def __init__(self, matrix_string):
        self.__matrix_rows = [[int(item) for item in row.split(' ')] for row in matrix_string.split('\n')]
        self.__matrix_columns = [list(column) for column in zip(*self.__matrix_rows)]

    def rows(self, big_list=[]):
        for item in range(len(self.__matrix_rows)):
            # print(self.__matrix_rows[item])
            for thing in self.__matrix_rows[item]:
                big_list.append(thing)
        print('rows: ', big_list)
        return big_list

    def columns(self, big_list=[]):
        for item in range(len(self.__matrix_columns)):
            # print(self.__matrix_columns[item])
            for thing in self.__matrix_columns[item]:
                big_list.append(thing)
        print('columns: ', big_list)
        return big_list



if __name__ == "__main__":
    input = '9 8 7\n5 3 2\n6 6 7'
    # add_rows(input)
    mat = Matrix_Rows_Columns(input)
    mat.rows()
    mat.columns()