''' Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. '''

# Restate: We are given an array of integers. Assuming there is exactly one solution,
# and without using the same element twice, find two numbers whose sum equals a target value.

# Questions: Are there duplicates? Are there negatives?
# Assumptions: No duplicates as that may be considered the same element twice.
# Yes negatives because those are integers too. 
# Pseudocode: 
# Naive solution would be to start with the first number and loop through the rest
# Stop if the number you're on is equal to the target minus the first number. 
# If no matches, move on to the second number and see its complement to the target appears. 

# using a hash table would reduce the look up time. Only one pass. 

# a longer solution...
# A better solution would look like something where we could quickly figure out
# where the complement would be if it were in the array somewhere. 
# If we sort the array, we can start by comparing either end to see if the number
# is even within bounds of the array. Then if we are larger than the given number 
# we move one index from the side with the larger number. If smaller, move an index
# from the smaller side. 

# ACCEPTED ANSWER:
class Solution:

    def twoSum(self, some_array, target):
        counter = 0
        for i in some_array:
            counter += 1
            ind = some_array.index(i)
            if target - i in some_array[ind+1:]:
                return [some_array.index(i), some_array[ind+1:].index(target-i) + counter]



                

def TwoSum_brute(some_array, target):
    counter = 0
    for i in some_array:
        counter += 1
        print(i)
        # print([some_array.index(i), some_array.index(target-i)])
        ind = some_array.index(i)
        # print('sliced ', some_array[ind+1:])
        if target - i in some_array[ind+1:]:
            # print('sliced ', some_array[ind+1:])
            print(some_array.index(i), some_array[ind+1:].index(target-i) + counter)
            return 

# you need to use a counter to find the index of the other element. .index finds the first element it sees


def TwoSumHash(some_array, target):
    buckets = [dict() for i in range(8)]
    print(buckets)
    buckets[5][5] = '4'
    print(buckets)
    buckets[5][5] = buckets[5][5] + '4'
    print(buckets)
    return



def TwoSum_func(someray, target):
    someray.sort()
    head = 0
    tail = len(someray) - 1
    found = False
    while not found:
        # print(head, tail)
        if someray[head] == someray[tail]:
            return None
        elif someray[head] + someray[tail] == target:
            found = True
        elif someray[head] + someray[tail] > target:
            tail -= 1
        elif someray[head] + someray[tail] < target:
            head += 1

    print(head, tail)
    return [head, tail]


TwoSum_brute([2,7,11,15], 9)
TwoSum_brute([3,2,4], 6)
TwoSum_brute([3,3], 6)

# TwoSum_func([2, 7, 11, 15], 9)
# TwoSum_func([3,2,4], 6)
# TwoSum_func([3,3], 6)

# TwoSumHash([0,4,5,4], 9)