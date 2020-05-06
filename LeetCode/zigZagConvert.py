
# The string "PAYPALISHIRING" is written in a zigzag pattern on a
#  given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# We just need to loop through the string and retrieve from those specific indexes

def zigZagCon(text, numrows):

    ''' TIME COMPLEXITY: O(n) because the function changes time based on the size
    of the input !!! ''' 

    # read every odd index character for each row. 
    counter = 0
    single_counter = 1
    single_index = 1
    for item in range(len(text[0])):
        # get the first item in each row
        if counter % 2 ==0:
            for row in text:
                string += item[counter]
            counter += 1
        else:
            if numrows % 2 != 0:
                if single_counter == 1:
                    string += text[numrows-1][single_index]
                    single_counter = 0
                    single_index += 1
                else:
                    string += text[numrows-2][single_index]
                    single_counter = 1
                    single_index += 2
            else:
                string += text[len(text)//2][single_index]
                single_index += 2
    return