'''Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.'''


def stackSubstring(my_string):
    stack = []
    max_string = []

    for char in my_string:
        print(f'char {char}')
        if char not in stack:
            stack.append(char)
            print(f'stack {stack}')
        else:
            print(f'stack size {len(stack)}, max_string {len(max_string)}')
            print(f'stack {stack}, max {max_string}')
            if len(stack) > len(max_string):
                max_string = []
                for item in stack:
                    max_string.append(item)
                print(f'max {max_string}')
            while char in stack:
                print(f'pop {stack.pop(0)}')
            stack.append(char)

    if len(stack) > len(max_string):
        max_string = stack

    print(f"len: {len(max_string)}, {max_string}")
    space = ''
    max_string = space.join(max_string)
    print(f"len: {len(max_string)}, {max_string}")
    return len(max_string)
input = 'pwwkew'
stackSubstring(input)


        
