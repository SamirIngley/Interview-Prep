# NEW SOLUTION: what we want it to do is 
# start a loop through each char. 
# search from the other end of the text til you find that char
# then check in between if it's a palindrome. 
# if not.. go on to the next letter.. if it is.. then that's the largest

def palindromIterative(text, right=-1, left=0):
    
 ''' TIME COMPLEXITY: O(n) because the function changes time based on the size
    of the input !!! ''' 

    max_len = 0
    curr_len = 0

    for char in text:

        if not char.isalpha() or not text[index].isalpha():
            continue

        # print(char_index, text[index])
        # print('abs ', abs(index+1))
        # print(char, text[index])
        if len(text)//2 <= abs(index+1):
            return True
        
        if char.lower() == text[index].lower():
            curr_len += 1
            index -= 1
        else:
            max_len = curr_len
            curr_len = 0
            index -=1

    return True