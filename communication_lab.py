

# 1. Given two arrays, determine if both arrays contain exactly the same elements, regardless of their order.
# 2. Given a string containing a long text, find the most commonly occurring word in the text as well as its count.
# 3. Given a sorted array, find the index of the first and last occurrence of a given element. If the given element is not found in the array, report that.
# 4. Given an array a of numbers and a target value t, find two numbers that sum to t (that is, a[i] + a[j] = t).




# 2. Restate: we are given a large string. We find the most commonly occuring word in the text & it's count. 
# loop through all the words, add them to a dictionary, and increase their counter by 1 as you add. 
# Return the key with the highest value (highest counter)

def highest_frequency(text, counter=1):
    freqs = {}

    for item in text:
        if item not in freqs.keys():
            freqs[item] == counter
        else:
            freqs[item] += counter

    

# 3. Restate: given a SORTED ARRAY, find the first and last occurence of an item and return their indexes. If not in array return DNE
# Loop through the array until element is found. 
# record element's index
# continue to loop through the array until element is no longer the target element.
# record index of last element. 
# Return Indexes or DNE

sorted_array = [1,2,3,4,5,6,7,7,8,9]

def first_last_indices(sorted_arr, target):
    first = None
    last = None
    for item in sorted_arr:
        if item == target and first == None:
            first = sorted_arr.index(item)
        elif first and not item == target:
            last = sorted_arr.index(item) - 1
        else:
            continue
    if first and last:
        return print(first,last)
    else:
        return print('DNE')

first_last_indices(sorted_array, 7)


# 4. sort the array then loop through each item and see if compliment (t-item) exists by binary searching 