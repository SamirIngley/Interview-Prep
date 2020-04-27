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

def medianTwoArrays(arr1, arr2):

    i_median = (len(arr1) + len(arr2)) / 2

    i_arr1= 0
    i_arr2= 0
    stack = []

    counter = 0
    flag = False

    while counter < i_median+1:
        print(counter, i_median+1)
        print(stack)
        # print(arr1[i_arr1], arr2[i_arr2])
        print(len(arr1))
        print(i_arr1)
        print(len(arr2))
        print(i_arr2)

        if int(len(arr1)) >= int(i_arr1+1) and int(len(arr2)) >= int(i_arr2+1):
            if arr1[i_arr1] == arr2[i_arr2]: 
                counter += 2
                stack.append(arr1[i_arr1])
                stack.append(arr2[i_arr2])
                i_arr1 += 1
                i_arr2 += 1

        if not len(arr1) >= 1+i_arr1:
            counter +=1
            stack.append(arr2[i_arr2])
            i_arr2 += 1
        elif not len(arr2) >= 1+i_arr2:
            counter += 1
            stack.append(arr1[i_arr1])
            i_arr1 += 1

        elif arr1[i_arr1] and arr1[i_arr1] < arr2[i_arr2]:
            counter += 1
            stack.append(arr1[i_arr1])
            i_arr1 += 1
        elif arr2[i_arr2] and arr1[i_arr1] > arr2[i_arr2]:
            counter += 1
            stack.append(arr2[i_arr2])
            i_arr2 += 1
        

    print('final', stack)
    print('counter', counter)

    if counter == i_median:
        print(stack[-1])
        return stack[-1]
    elif counter-1 <= i_median:
        print(stack[-2], stack[-1])
        print((stack[-2]+stack[-1])/2)
        return stack[-2]/stack[-1]
    else:
        print(stack, i_median)
   



ray1 = [1, 2]          
ray2 = [3, 4]
medianTwoArrays(ray1, ray2)





