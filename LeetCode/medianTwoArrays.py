'''There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5'''



def medianArrays(arr1, arr2):

    stack = []
    counter = 0
    i_arr1 = 0
    i_arr2 = 0
    median = (len(arr1) + len(arr2)) // 2
    print('median ', median)

    while len(stack) < (median + 1): # while we have not crossed the median, keep adding to the stack

        # if they're both the same value, counter + 2 and both indexes + 1
        if int(len(arr1)) >= int(i_arr1+1) and int(len(arr2)) >= int(i_arr2+1):
            if arr1[i_arr1] == arr2[i_arr2]: 
                counter += 2
                stack.append(arr1[i_arr1])
                stack.append(arr2[i_arr2])
                i_arr1 += 1
                i_arr2 += 1

        # if index is beyond array length, start the next array
        if not len(arr1) >= 1+i_arr1:
            counter +=1
            stack.append(arr2[i_arr2])
            i_arr2 += 1

        # if other index is beyond other array length, start the other array
        elif not len(arr2) >= 1+i_arr2:
            counter += 1
            stack.append(arr1[i_arr1])
            i_arr1 += 1

        # compare which item in each array is larger and append that one, and add to counter
        elif arr1[i_arr1] and arr1[i_arr1] < arr2[i_arr2]:
            counter += 1
            stack.append(arr1[i_arr1])
            i_arr1 += 1
        elif arr2[i_arr2] and arr1[i_arr1] > arr2[i_arr2]:
            counter += 1
            stack.append(arr2[i_arr2])
            i_arr2 += 1
    
    print('stack', stack)
    print(stack[median])
        
    if (len(arr1) + len(arr2)) % 2 == 0: # even nums, split two values
        print((stack[median]+stack[median-1])/2)
        return ((stack[median]+stack[median-1])/2)
    else: # odd, get one value
        print(stack[median])
        return stack[median]



ray1 = [0,0]          
ray2 = [0,0]
medianArrays(ray1, ray2)





# def medianTwoArrays(arr1, arr2):

#     i_median = (len(arr1) + len(arr2)) / 2

#     i_arr1= 0
#     i_arr2= 0
#     stack = []

#     counter = 0
#     flag = False

#     # count if we're at the median, two greater than median bc we need the median and next value in case there we need their middle
#     while counter < i_median+2:
#         print(counter, i_median+2)
#         print(stack)
#         # print(arr1[i_arr1], arr2[i_arr2])
#         print(len(arr1))
#         print(i_arr1)
#         print(len(arr2))
#         print(i_arr2)

#         # if they're both the same value, counter + 2 and both indexes + 1
#         if int(len(arr1)) >= int(i_arr1+1) and int(len(arr2)) >= int(i_arr2+1):
#             if arr1[i_arr1] == arr2[i_arr2]: 
#                 counter += 2
#                 stack.append(arr1[i_arr1])
#                 stack.append(arr2[i_arr2])
#                 i_arr1 += 1
#                 i_arr2 += 1

#         # if index is beyond array length, start the next array
#         if not len(arr1) >= 1+i_arr1:
#             counter +=1
#             stack.append(arr2[i_arr2])
#             i_arr2 += 1

#         # if index is beyond array length, start the next array
#         elif not len(arr2) >= 1+i_arr2:
#             counter += 1
#             stack.append(arr1[i_arr1])
#             i_arr1 += 1

#         # compare which item in each array is larger and append that one, and add to counter
#         elif arr1[i_arr1] and arr1[i_arr1] < arr2[i_arr2]:
#             counter += 1
#             stack.append(arr1[i_arr1])
#             i_arr1 += 1
#         elif arr2[i_arr2] and arr1[i_arr1] > arr2[i_arr2]:
#             counter += 1
#             stack.append(arr2[i_arr2])
#             i_arr2 += 1
        

#     print('final', stack)
#     print('counter', counter)

#     # counter got either 1 or 2 added to it in which case it was no longer larger than the i_median
#     # counter is either equal to i_median or
#     if counter-2 == i_median:
#         if (len(arr1) + len(arr2)) % 2 == 0: # if even
#             print(stack[-1])
#             return stack[-1]
#         else:
#             return stack

#     # counter is one more than the median
#     elif counter-1 <= i_median:
#         print(stack[-2], stack[-1])
#         print((stack[-2]+stack[-1])/2)
#         return stack[-2]/stack[-1]
#     else:
#         print(stack, i_median)
   



# ray1 = [1, 3]          
# ray2 = [2]
# medianTwoArrays(ray1, ray2)
