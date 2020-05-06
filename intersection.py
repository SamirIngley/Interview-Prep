''' Write a function that uses a hash table(dictionary) to find the 
intersection between two unsorted arrays (lists) and return the elements
they have in common as a list. What are the drawbacks of this solution? '''

input1 = [1,5,6,9]
input2 = [3,4,6,10,9]

def intersect(arr1, arr2):
    buckets1 = {}
    buckets2 = {}

    for item in arr1:
        bucket = hash(item) % 10
        bucket1[bucket] 